import logging
import logging.handlers

from flask import render_template, abort, request
from jinja2 import TemplateNotFound

from baseblueprint import BaseBlueprint
from sha_algo import SHA as SHA_algo

"""The class below is a blueprint loaded by Flask. See baseblueprint.py for
more info"""

class SHABlueprint(BaseBlueprint):

    def __init__(self):

        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log',
                                                  maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)

        self.algo = SHA_algo()

        url = "/sha"
        super().__init__('SHA', 'HASHING', url)

        self.add_url_rule(url, "sha", self.SHA)
        self.add_url_rule(url + "/encryption", "sha_encryption", self.displayEncryptedText, methods=["POST"])



    def SHA(self):

        """This method is called when a request is sent to /sha"""

        try:

            return render_template("sha.html", allAlgos=self._allAlgosSorted,
                                   historicalAlgos=self._historicalAlgosSorted,
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)

        except TemplateNotFound:

            abort(404)



    def displayEncryptedText(self):

        """This method is called when a request is sent to /sha/encryption"""

        message = request.form["message"]
        encryptedText = str(self.algo.encrypt(message))

        try:

            return render_template("sha.html",
                                   mode="displayEncryptedText",
                                   encryptedMessage=encryptedText,
                                   allAlgos=self._allAlgosSorted,
                                   historicalAlgos=self._historicalAlgosSorted,
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)

        except TemplateNotFound:

            abort(404)
