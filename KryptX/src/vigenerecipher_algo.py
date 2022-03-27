"""Implementation of the Vigenere cipher enryption method (use of interwoven
Caesar ciphers)"""

import logging
import logging.handlers
from encryptioninterface import EncryptionInterface


class VigenereCipher(EncryptionInterface):

    def __init__(self):

        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log', maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)
        VigenereCipher.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def encrypt(self, message, key=0):

        if not isinstance(message, str):

            self.logger.error("Error during the encryption of a message with the Vigenere cipher. The message must be a string")
            return False

        elif not isinstance(key, str):

            self.logger.error("Error during the encryption of a message with the Vigenere cipher. The key must be an string")
            return False

        elif key == "":

            self.logger.error("Error during the encryption of a message with the Vigenere cipher. The key cannot be an empty string")
            return False

        newKey = ""

        for i in range(0, len(key)):

            if key[i].lower() not in VigenereCipher.alphabet:

                self.logger.error("Error during the encryption of a message with the Vigenere cipher. The key cannot contain accents or special characters")
                return False

            newKey = newKey + key[i].lower()

        key = newKey

        encryptedMessage = ""

        key = self.prepareKey(key, len(message))


        for i, j in zip(message, key):

            if i.lower() in VigenereCipher.alphabet:

                try:

                    newIndex = (VigenereCipher.alphabet.index(i.lower()) + VigenereCipher.alphabet.index(j.lower())) % len(VigenereCipher.alphabet)

                except ValueError:

                    self.logger.error("Error during the encryption of a message with the Vigenere cipher. One of the letters in the message could not be found in the alphabet")
                    return False

                if i.isupper():

                    encryptedMessage = encryptedMessage + VigenereCipher.alphabet[newIndex].capitalize()

                else:

                    encryptedMessage = encryptedMessage + VigenereCipher.alphabet[newIndex]

            else:

                encryptedMessage = encryptedMessage + i

        return encryptedMessage


    def decrypt(self, message, key=0):

        if not isinstance(message, str):

            self.logger.error("Error during the decryption of a message with the Vigenere cipher. The message must be a string")
            return False

        elif not isinstance(key, str):

            self.logger.error("Error during the decryption of a message with the Vigenere cipher. The key must be an string")
            return False

        elif key == "":

            self.logger.error("Error during the decryption of a message with the Vigenere cipher. The key cannot be an empty string")
            return False

        newKey = ""

        for i in range(0, len(key)):

            if key[i].lower() not in VigenereCipher.alphabet:

                self.logger.error("Error during the decryption of a message with the Vigenere cipher. The key cannot contain accents or special characters")
                return False

            newKey = newKey + key[i].lower()

        key = newKey

        decryptedMessage = ""

        key = self.prepareKey(key, len(message))


        for i, j in zip(message, key):

            if i.lower() in VigenereCipher.alphabet:

                try:

                    newIndex = (VigenereCipher.alphabet.index(i.lower()) - VigenereCipher.alphabet.index(j.lower())) % len(VigenereCipher.alphabet)

                except ValueError:

                    self.logger.error("Error during the decryption of a message with the Vigenere cipher. One of the letters in the encrypted message could not be found in the alphabet")
                    return False

                if i.isupper():

                    decryptedMessage = decryptedMessage + VigenereCipher.alphabet[newIndex].capitalize()

                else:

                    decryptedMessage = decryptedMessage + VigenereCipher.alphabet[newIndex]

            else:

                decryptedMessage = decryptedMessage + i

        return decryptedMessage

    def prepareKey(self, key, messageLength):

        if len(key) == messageLength:

            return key

        elif len(key) > messageLength:

            while len(key) != messageLength:

                key = key[:-1]

            return key



        originalKey = key

        while len(key) != messageLength:

            for i in originalKey:

                key = key + i

                if len(key) == messageLength:

                    break
        return key
