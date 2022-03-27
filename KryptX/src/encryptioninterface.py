"""Common interface class for all the encryption modules"""

from abc import ABC, abstractmethod

class EncryptionInterface(ABC):

    @abstractmethod
    def encrypt(self, message, key=0):

        """message: message to be decrypted. Expects a string
        key: key to be used to decrypt the message. Its type depends on
        the specific algorithm used"""
        pass

    @abstractmethod
    def decrypt(self, message, key=0):

        """message: message to be decrypted. Expects a bytes object
        key: key to be used to decrypt the message. Its type depends on
        the specific algorithm used"""
        pass
