"""Implementation of the Caesar cipher encryption method (encryption through a
 simple shift of letters in the alphabet)"""

import logging
import logging.handlers
from encryptioninterface import EncryptionInterface

class CaesarCipher(EncryptionInterface):

    def __init__(self):

        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log', maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)
        CaesarCipher.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def encrypt(self, message, key=0):

        if not isinstance(message, str):

            self.logger.error("Error during the encryption of a message with the Caesar cipher. The message must be a string")
            return False

        if not isinstance(key, int):

            self.logger.error("Error during the encryption of a message with the Caesar cipher. The key must be an int")
            return False

        encryptedMessage = ""

        for i in message:

            if i.lower() in CaesarCipher.alphabet:

                try:

                    newIndex = CaesarCipher.alphabet.index(i.lower()) + key

                except ValueError:

                    self.logger.error("Error during the encryption of a message with the Caesar cipher. One of the letters in the message could not be found in the alphabet")
                    return False

                newIndex = newIndex % len(CaesarCipher.alphabet)

                if i.isupper():

                    encryptedMessage = encryptedMessage + CaesarCipher.alphabet[newIndex].capitalize()

                else:

                    encryptedMessage = encryptedMessage + CaesarCipher.alphabet[newIndex]

            else:

                encryptedMessage = encryptedMessage + i

        return encryptedMessage

    def decrypt(self, message, key=0):

        if not isinstance(message, str):

            self.logger.error("Error during the decryption of a message with the Caesar cipher. The message must be a string")
            return False

        if not isinstance(key, int):

            self.logger.error("Error during the decryption of a message with the Caesar cipher. The key must be an int")
            return False


        decryptedMessage = ""

        for i in message:

            if i.lower() in CaesarCipher.alphabet:

                try:

                    newIndex = CaesarCipher.alphabet.index(i.lower()) - key

                except ValueError:

                    self.logger.error("Error during the encryption of a message with the Caesar cipher. One of the letters in the encrypted message could not be found in the alphabet")
                    return False

                newIndex = newIndex % len(CaesarCipher.alphabet)

                if i.isupper():

                    decryptedMessage = decryptedMessage + CaesarCipher.alphabet[newIndex].capitalize()

                else:

                    decryptedMessage = decryptedMessage + CaesarCipher.alphabet[newIndex]

            else:

                decryptedMessage = decryptedMessage + i

        return decryptedMessage
