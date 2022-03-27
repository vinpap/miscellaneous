"""Implementation of the RSA encryption method"""

import logging
import logging.handlers
import base64
import binascii
from Crypto.PublicKey import RSA
from encryptioninterface import EncryptionInterface


class RSAAlgo(EncryptionInterface):

    def __init__(self):

        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log', maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)


    def encrypt(self, message, key=0):

        if not isinstance(message, str):

            self.logger.error("Error during the encryption of a message with RSA. The message must be a string")
            return False

        if not isinstance(key, str):

            self.logger.error("Error during the encryption of a message with RSA. The key must be a string")
            return False


        key = bytes(key, "utf-8")

        # The code below returns 0 if the key is not valid

        try:

            publicKey = RSA.importKey(key)

        except ValueError:

            return 0

        message = bytes(message, "utf-8")

        encryptedMessage = publicKey.encrypt(message, b"random")
        encryptedMessage = base64.b64encode(encryptedMessage[0])


        return encryptedMessage.decode("utf-8")

    def decrypt(self, message, key=0):


        if not isinstance(message, str):

            self.logger.error("Error during the decryption of a message with RSA. The message must be a string")
            return False

        if not isinstance(key, str):

            self.logger.error("Error during the decryption of a message with RSA. The key must be a string")
            return False

        message = message.encode("utf-8")

        # The code below returns 1 if the encrypted message is not encoded in Base 64

        try:

            message = base64.b64decode(message)

        except binascii.Error:

            return 1

        key = bytes(key, "utf-8")

        # The code below returns 0 if the key is not valid

        try:

            privateKey = RSA.importKey(key)

        except ValueError:

            return 0

        decryptedMessage = privateKey.decrypt(message)

        return decryptedMessage.decode("utf-8")

    def generateKeysPair(self):

        newKey = RSA.generate(4096, e=65537)
        privateKey = newKey.exportKey("PEM")
        publicKey = newKey.publickey().exportKey("PEM")


        privateKey = privateKey.decode("utf-8")
        publicKey = publicKey.decode("utf-8")

        return (privateKey, publicKey)
