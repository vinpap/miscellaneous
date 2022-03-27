import logging
import logging.handlers

from flask import render_template, abort, request
from jinja2 import TemplateNotFound

from baseblueprint import BaseBlueprint
from md5_algo import MD5

"""The class below is a blueprint loaded by Flask. See baseblueprint.py for
more info"""

class MD5Blueprint(BaseBlueprint):

    def __init__(self):

        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log',
                                                  maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)

        self.algo = MD5()

        url = "/md5"
        super().__init__('MD5', 'HASHING', url)

        self.add_url_rule(url, "md5", self.MD5)
        self.add_url_rule(url + "/encryption", "des_encryption", self.displayEncryptedText, methods=["POST"])


    def MD5(self):

        """This method is called when a request is sent to /md5"""

        try:

            return render_template("md5.html", allAlgos=self._allAlgosSorted,
                                   historicalAlgos=self._historicalAlgosSorted,
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)

        except TemplateNotFound:

            abort(404)


    def displayEncryptedText(self):

        """This method is called when a request is sent to /md5/encryption"""

        message = request.form["message"]
        encryptedText = str(self.algo.encrypt(message))

        try:

            return render_template("md5.html",
                                   mode="displayEncryptedText",
                                   encryptedMessage=encryptedText,
                                   allAlgos=self._allAlgosSorted,
                                   historicalAlgos=self._historicalAlgosSorted,
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)

        except TemplateNotFound:

            abort(404)
