"""Implementation of the Enigma encryption method (M3 version used by the
German navy)"""

import logging
import logging.handlers
from pycipher import Enigma
from encryptioninterface import EncryptionInterface

class EnigmaM3(EncryptionInterface):

    def __init__(self):

        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log', maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)


    def encrypt(self, message, key=0):

        """key parameter is a table made of four elements:
       - a tuple of three chars for the rotors start position
       - a tuple of three int for the rotors used
       - a tuple of three chars for the ring settings
       - a list of 10 tuples of two chars (at most) for the plugboard settings"""

        if not isinstance(message, str):

            self.logger.error("Error during the encryption of a message with Enigma. The message must be a string")
            return False

        if not self.checkKeyFormat(key):

            self.logger.error("Error during the encryption of a message with Enigma. The settings provided do not follow the right format")
            return False


        encryptedText = Enigma(settings=key[0], rotors=key[1], reflector='B',
                               ringstellung=key[2], steckers=key[3]).encipher(message)

        return encryptedText


    def decrypt(self, message, key=0):

        """key parameter is a table made of four elements:
       - a tuple of three chars for the rotors start position
       - a tuple of three int for the rotors used
       - a tuple of three chars for the ring settings
       - a list of 10 tuples of two chars (at most) for the plugboard settings"""

        if not isinstance(message, str):

            self.logger.error("Error during the decryption of a message with Enigma. The message must be a string")
            return False

        if not self.checkKeyFormat(key):

            self.logger.error("Error during the decryption of a message with Enigma. The settings provided do not follow the right format")
            return False


        decryptedText = Enigma(settings=key[0], rotors=key[1], reflector='B',
                               ringstellung=key[2], steckers=key[3]).decipher(message)

        return decryptedText

    def checkKeyFormat(self, key):

        if (not isinstance(key, list) or len(key) != 4):

            return False

        for i in key:

            if (not isinstance(i, tuple)) and (not isinstance(i, list)):

                return False

        return True
