import logging
import logging.handlers

from flask import render_template, abort, request
from jinja2 import TemplateNotFound

from baseblueprint import BaseBlueprint
from vigenerecipher_algo import VigenereCipher

"""The class below is a blueprint loaded by Flask. See baseblueprint.py for
more info"""

class VigenereCipherBlueprint(BaseBlueprint):

    def __init__(self):

        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log',
                                                  maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)

        self.algo = VigenereCipher()

        url = "/vigenerecipher"
        super().__init__('Vigenère Cipher', 'HISTORICAL', url)

        self.add_url_rule(url, "vigenerecipher", self.vigenereCipher)
        self.add_url_rule(url + "/encryption", "vigenere_cipher_encryption", self.displayEncryptedText, methods=["POST"])
        self.add_url_rule(url + "/decryption", "vigenere_cipher_decryption", self.displayDecryptedText, methods=["POST"])

    def vigenereCipher(self):

        """This method is called when a request is sent to /vigenerecipher"""

        try:

            return render_template("vigenerecipher.html",
                                   mode="homepage",
                                   allAlgos=self._allAlgosSorted,
                                   historicalAlgos=self._historicalAlgosSorted,
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)

        except TemplateNotFound:

            abort(404)


    def displayEncryptedText(self):

        """This method is called when a request is sent to /vigenerecipher/encryption"""

        message = request.form["message"]
        key = request.form["key_area"]

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for i in key:

            if i.lower() not in alphabet:

                errorMsg = ("This key is not valid. The key can only contain "
                            "alphabet letters without accents")

                try:

                    return render_template("vigenerecipher.html",
                                           mode="encryptionError",
                                           error=errorMsg,
                                           allAlgos=self._allAlgosSorted,
                                           historicalAlgos=self._historicalAlgosSorted,
                                           outdatedAlgos=self._outdatedAlgosSorted,
                                           modernAlgos=self._modernAlgosSorted,
                                           hashingAlgos=self._hashingAlgosSorted)

                except TemplateNotFound:

                    abort(404)

        encryptedText = str(self.algo.encrypt(message, key))

        try:

            return render_template("vigenerecipher.html",
                                   mode="displayEncryptedText",
                                   encryptedMessage=encryptedText,
                                   allAlgos=self._allAlgosSorted,
                                   historicalAlgos=self._historicalAlgosSorted,
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)

        except TemplateNotFound:

            abort(404)


    def displayDecryptedText(self):

        """This method is called when a request is sent to /vigenerecipher/decryption"""

        message = request.form["message"]
        key = request.form["key_area"]

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for i in key:

            if i.lower() not in alphabet:

                errorMsg = ("This key is not valid. The key can only contain "
                            "alphabet letters without accents")

                try:

                    return render_template("vigenerecipher.html",
                                       mode="decryptionError",
                                       error=errorMsg,
                                       allAlgos=self._allAlgosSorted,
                                       historicalAlgos=self._historicalAlgosSorted,
                                       outdatedAlgos=self._outdatedAlgosSorted,
                                       modernAlgos=self._modernAlgosSorted,
                                       hashingAlgos=self._hashingAlgosSorted)

                except TemplateNotFound:

                    abort(404)

        decryptedText = self.algo.decrypt(message, key)

        try:

            return render_template("vigenerecipher.html",
                                   mode="displayDecryptedText",
                                   decryptedMessage=decryptedText,
                                   allAlgos=self._allAlgosSorted,
                                   historicalAlgos=self._historicalAlgosSorted,
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)

        except TemplateNotFound:

            abort(404)
            