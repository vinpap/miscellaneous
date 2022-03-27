import logging
import logging.handlers
from Crypto.Cipher import AES
from Crypto.Util import Counter
from encryptioninterface import EncryptionInterface


"""Implementation of the AES encryption method"""


class AdvancedEncryptionStandard(EncryptionInterface):

    def __init__(self):

        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log', maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)


    def encrypt(self, message, key=0):


        if not isinstance(message, str):

            self.logger.error("Error during the encryption of a message with DES. The message must be a string")
            return False

        if not isinstance(key, str) or len(bytes(key, encoding='utf-8')) not in (16, 24, 32):

            self.logger.error("Error during the encryption of a message with DES. The key must be a string in ASCII format of length 16, 24 or 32")
            return False

        userKey = bytes(key, encoding='utf-8')
        ctr = Counter.new(128)
        encryptor = AES.new(userKey, AES.MODE_CTR, counter=ctr)
        encryptedMessage = encryptor.encrypt(message)


        return encryptedMessage.hex()

    def decrypt(self, message, key=0):


        if not isinstance(message, str):

            self.logger.error("Error during the decryption of a message with DES. The message must be a string")
            return False

        if not isinstance(key, str) or len(bytes(key, encoding='utf-8')) not in (16, 24, 32):

            self.logger.error("Error during the decryption of a message with DES. The key must be an string in ASCII format of length 16, 24 or 32")
            return False

        userKey = bytes(key, encoding='utf-8')

        # The section below checks if the encrypted message is encoded in hexa

        try:

            message = bytes.fromhex(message)

        except ValueError:

            return 1

        ctr = Counter.new(128)
        decryptor = AES.new(userKey, AES.MODE_CTR, counter=ctr)
        decryptedMessage = decryptor.decrypt(message)

        # When the key given for the decryption is wrong, a UnicodeDecodeError
        # exception is often raised when we try to decode the decrypted message
        # (which should be encoded in UTF-8). The code below handles the
        # exception so that the method returns 0 and the app does not crash.

        try:

            return decryptedMessage.decode("utf-8")

        except UnicodeDecodeError:

            return 0
