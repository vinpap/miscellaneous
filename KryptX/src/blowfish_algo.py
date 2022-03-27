import logging
import logging.handlers
from operator import xor
import os
import blowfish
from encryptioninterface import EncryptionInterface


"""Implementation of the RSA encryption method"""


class Blowfish(EncryptionInterface):

    def __init__(self):

        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log', maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)

        self.nonce = int.from_bytes(os.urandom(8), "big")


    def encrypt(self, message, key=0):


        if not isinstance(message, str):

            self.logger.error("Error during the encryption of a message with Blowfish. The message must be a string")
            return False

        if not isinstance(key, str) or len(bytes(key, encoding='utf-8')) < 4 or len(bytes(key, encoding='utf-8')) > 56:

            self.logger.error("Error during the encryption of a message with Blowfish. The key must be between 4 and 56 bytes long")

            return False


        cipher = blowfish.Cipher(bytes(key, encoding='utf-8'))
        encryptionCounter = blowfish.ctr_counter(self.nonce, f=xor)

        encryptedMessage = b"".join(cipher.encrypt_ctr(bytes(message, encoding="utf-8"), encryptionCounter))

        return encryptedMessage.hex()

    def decrypt(self, message, key=0):


        if not isinstance(message, str):

            self.logger.error("Error during the decryption of a message with Blowfish. The message must be a string")
            return False

        if not isinstance(key, str) or len(bytes(key, encoding='utf-8')) < 4 or len(bytes(key, encoding='utf-8')) > 56:

            self.logger.error("Error during the decryption of a message with Blowfish. The key must be between 4 and 56 bytes long")
            return False
        
        # The section below checks if the encrypted message is encoded in hexa
        
        try:
            
            message = bytes.fromhex(message)
        
        except ValueError: 
            
            return 1
        

        cipher = blowfish.Cipher(bytes(key, encoding='utf-8'))

        decryptionCounter = blowfish.ctr_counter(self.nonce, f=xor)

        decryptedMessage = b"".join(cipher.decrypt_ctr(message, decryptionCounter))

        # When the key given for the decryption is wrong, a UnicodeDecodeError
        # exception is often raised when we try to decode the decrypted message
        # (which should be encoded in UTF-8). The code below handles the
        # exception so that the method returns 0 and the app does not crash.

        try:
            
            return decryptedMessage.decode("utf-8")
        
        except UnicodeDecodeError:
            
            return 0
    