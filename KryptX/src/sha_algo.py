"""Implementation of the SHA512 hashing function"""

import logging
import logging.handlers
import hashlib
from encryptioninterface import EncryptionInterface


class SHA(EncryptionInterface):

    def __init__(self):

        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log', maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)


    def encrypt(self, message, key=0):


        if not isinstance(message, str):

            self.logger.error("Error during the hashing of a message with SHA512. The message must be a string")
            return False

        result = hashlib.sha512(message.encode())

        return result.hexdigest()

    def decrypt(self, message, key=0):

        return False
