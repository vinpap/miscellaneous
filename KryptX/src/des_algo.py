"""Implementation of the DES and TripleDES encryption methods"""

import logging
import logging.handlers
from des import DesKey
from encryptioninterface import EncryptionInterface


class DES(EncryptionInterface):

    def __init__(self):

        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log', maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)


    def encrypt(self, message, key=0):


        """The key parameter must be an ASCII string of length 8, 16 or 24"""


        if not isinstance(message, str):

            self.logger.error("Error during the encryption of a message with DES. The message must be a string")
            return False

        if not isinstance(key, str) or len(bytes(key, encoding='utf-8')) not in (8, 16, 24):

            self.logger.error("Error during the encryption of a message with DES. The key must be a string in ASCII format of length 8, 16 or 24")
            return False

        userKey = DesKey(bytes(key, encoding='utf-8'))

        encryptedMessage = userKey.encrypt(bytes(message, encoding='utf-8'), padding=True)
        print(encryptedMessage)

        return encryptedMessage.hex()

    def decrypt(self, message, key=0):

        """The key parameter must be an ASCII string of length 8, 16 or 24"""

        if not isinstance(message, str):

            self.logger.error("Error during the decryption of a message with DES. The message must be a string")
            return False

        if not isinstance(key, str) or len(bytes(key, encoding='utf-8')) not in (8, 16, 24):

            self.logger.error("Error during the decryption of a message with DES. The key must be an string in ASCII format of length 8, 16 or 24")
            return False

        # The section below checks if the encrypted message is encoded in hexa

        try:

            message = bytes.fromhex(message)

        except ValueError:

            return 1

        userKey = DesKey(bytes(key, encoding='utf-8'))
        decryptedMessage = userKey.decrypt(message, padding=True)

        # When the key given for the decryption is wrong, a UnicodeDecodeError
        # exception is often raised when we try to decode the decrypted message
        # (which should be encoded in UTF-8). The code below handles the
        # exception so that the method returns 0 and the app does not crash.

        try:

            decryptedMessage = decryptedMessage.decode("utf-8")

        except UnicodeDecodeError:

            return 0

        if len(decryptedMessage) == 0: # Happens when the key is wrong

            return 0

        return decryptedMessage
