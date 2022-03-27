import logging
import logging.handlers

from flask import render_template, abort, request
from jinja2 import TemplateNotFound

from baseblueprint import BaseBlueprint
from blowfish_algo import Blowfish

"""The class below is a blueprint loaded by Flask. See baseblueprint.py for
more info"""

class BlowfishBlueprint(BaseBlueprint):

    def __init__(self):

        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log',
                                                  maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)

        self.algo = Blowfish()

        url = "/blowfish"
        super().__init__('Blowfish', 'MODERN', url)

        self.add_url_rule(url, "blowfish", self.blowfish)
        self.add_url_rule(url + "/encryption", "blowfish_encryption", self.displayEncryptedText, methods=["POST"])
        self.add_url_rule(url + "/decryption", "blowfish_decryption", self.displayDecryptedText, methods=["POST"])


    def blowfish(self):

        """This method is called when a request is sent to /blowfish"""

        try:

            return render_template("blowfish.html",
                                   mode="homepage",
                                   allAlgos=self._allAlgosSorted,
                                   historicalAlgos=self._historicalAlgosSorted,
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)

        except TemplateNotFound:

            abort(404)


    def displayEncryptedText(self):

        """This method is called when a request is sent to /blowfish/encryption"""

        message = request.form["message"]
        key = request.form["key_area"]



        if len(bytes(key, encoding='utf-8')) not in range(4, 56):

            errorMsg = ("This key is not valid. The key must be between "
                        "32 and 448 bits (4 and 56 characters in ASCII format)")
            try:

                return render_template("blowfish.html",
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

            return render_template("blowfish.html",
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

        """This method is called when a request is sent to /blowfish/decryption"""

        message = request.form["message"]
        key = request.form["key_area"]

        if len(bytes(key, encoding='utf-8')) not in range(4, 56):

            errorMsg = ("This key is not valid. The key must be between "
                        "32 and 448 bits (4 and 56 characters in ASCII format)")
            try:

                return render_template("blowfish.html",
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

        if decryptedText == 0: # If the key provided is wrong

            errorMsg = ("Error during the decryption of the message. Please make"
                       " sure you are using a valid key")

            try:

                return render_template("blowfish.html",
                                   mode="decryptionError",
                                   error=errorMsg,
                                   allAlgos=self._allAlgosSorted,
                                   historicalAlgos=self._historicalAlgosSorted,
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)

            except TemplateNotFound:

                abort(404)

        elif decryptedText == 1: # If the encoded message is not in hexa

            errorMsg = ("Error during the decryption of the message. Please make"
                       " sure the message you want to decrypt is encoded in"
                       " hexadecimal")

            try:

                return render_template("blowfish.html",
                                   mode="decryptionError",
                                   error=errorMsg,
                                   allAlgos=self._allAlgosSorted,
                                   historicalAlgos=self._historicalAlgosSorted,
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)

            except TemplateNotFound:

                abort(404)



        try:

            return render_template("blowfish.html",
                                   mode="displayDecryptedText",
                                   decryptedMessage=decryptedText,
                                   allAlgos=self._allAlgosSorted,
                                   historicalAlgos=self._historicalAlgosSorted,
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)

        except TemplateNotFound:

            abort(404)
