import logging
import logging.handlers

from flask import render_template, abort, request
from jinja2 import TemplateNotFound

from baseblueprint import BaseBlueprint
from enigmam3_algo import EnigmaM3

"""The class below is a blueprint loaded by Flask. See baseblueprint.py for
more info"""

class EnigmaM3Blueprint(BaseBlueprint):

    def __init__(self):

        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log',
                                                  maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)

        self.algo = EnigmaM3()

        url = "/enigmam3"
        super().__init__('Enigma M3', 'HISTORICAL', url)

        self.add_url_rule(url, "enigmam3", self.enigmam3)
        self.add_url_rule(url + "/encryption", "enigmam3_encryption", self.displayEncryptedText, methods=["POST"])
        self.add_url_rule(url + "/decryption", "enigmam3_decryption", self.displayDecryptedText, methods=["POST"])


    def enigmam3(self):

        """This method is called when a request is sent to /enigmam3"""

        try:

            return render_template("enigmam3.html",
                                   mode="homepage",
                                   allAlgos=self._allAlgosSorted,
                                   historicalAlgos=self._historicalAlgosSorted,
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)

        except TemplateNotFound:

            abort(404)


    def displayEncryptedText(self):

        """This method is called when a request is sent to /enigmam3/encryption"""

        message = request.form["message"]


        settings = []
        settings.append((request.form["first_rotor_start"], request.form["second_rotor_start"], request.form["third_rotor_start"]))
        settings.append((int(request.form["first_rotor_used"]), int(request.form["second_rotor_used"]), int(request.form["third_rotor_used"])))
        settings.append((request.form["ring_settings_1"], request.form["ring_settings_2"], request.form["ring_settings_3"]))

        settings.append([
            (request.form["plugboard_settings_1_1"],
            request.form["plugboard_settings_1_2"]),
            (request.form["plugboard_settings_2_1"],
            request.form["plugboard_settings_2_2"]),
            (request.form["plugboard_settings_3_1"],
            request.form["plugboard_settings_3_2"]),
            (request.form["plugboard_settings_4_1"],
            request.form["plugboard_settings_4_2"]),
            (request.form["plugboard_settings_5_1"],
            request.form["plugboard_settings_5_2"]),
            (request.form["plugboard_settings_6_1"],
            request.form["plugboard_settings_6_2"]),
            (request.form["plugboard_settings_7_1"],
            request.form["plugboard_settings_7_2"]),
            (request.form["plugboard_settings_8_1"],
            request.form["plugboard_settings_8_2"]),
            (request.form["plugboard_settings_9_1"],
            request.form["plugboard_settings_9_2"]),
            (request.form["plugboard_settings_10_1"],
            request.form["plugboard_settings_10_2"])
            ])

        self.logger.info("Message: ")
        self.logger.info(message)
        self.logger.info("Settings: ")
        self.logger.info(str(settings))



        encryptedText = str(self.algo.encrypt(message, settings))

        try:

            return render_template("enigmam3.html",
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

        """This method is called when a request is sent to /enigmam3/decryption"""

        message = request.form["message"]


        settings = []
        settings.append((request.form["first_rotor_start"], request.form["second_rotor_start"], request.form["third_rotor_start"]))
        settings.append((int(request.form["first_rotor_used"]), int(request.form["second_rotor_used"]), int(request.form["third_rotor_used"])))
        settings.append((request.form["ring_settings_1"], request.form["ring_settings_2"], request.form["ring_settings_3"]))

        settings.append([
            (request.form["plugboard_settings_1_1"],
            request.form["plugboard_settings_1_2"]),
            (request.form["plugboard_settings_2_1"],
            request.form["plugboard_settings_2_2"]),
            (request.form["plugboard_settings_3_1"],
            request.form["plugboard_settings_3_2"]),
            (request.form["plugboard_settings_4_1"],
            request.form["plugboard_settings_4_2"]),
            (request.form["plugboard_settings_5_1"],
            request.form["plugboard_settings_5_2"]),
            (request.form["plugboard_settings_6_1"],
            request.form["plugboard_settings_6_2"]),
            (request.form["plugboard_settings_7_1"],
            request.form["plugboard_settings_7_2"]),
            (request.form["plugboard_settings_8_1"],
            request.form["plugboard_settings_8_2"]),
            (request.form["plugboard_settings_9_1"],
            request.form["plugboard_settings_9_2"]),
            (request.form["plugboard_settings_10_1"],
            request.form["plugboard_settings_10_2"])
            ])

        self.logger.info("Message: ")
        self.logger.info(message)
        self.logger.info("Settings: ")
        self.logger.info(str(settings))


        decryptedText = self.algo.decrypt(message, settings)

        try:

            return render_template("enigmam3.html",
                                   mode="displayDecryptedText",
                                   decryptedMessage=decryptedText,
                                   allAlgos=self._allAlgosSorted,
                                   historicalAlgos=self._historicalAlgosSorted,
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)

        except TemplateNotFound:

            abort(404)
