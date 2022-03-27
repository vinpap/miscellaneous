"""Main server module. This class manages the homepage and loads all the
blueprints (one encryption method = one blueprint)"""

import logging
import logging.handlers

from flask import Flask, render_template, abort
from jinja2 import TemplateNotFound

from aes_blueprint import AESBlueprint
from blowfish_blueprint import BlowfishBlueprint
from caesarcipher_blueprint import CaesarCipherBlueprint
from des_blueprint import DESBlueprint
from enigmam3_blueprint import EnigmaM3Blueprint
from md5_blueprint import MD5Blueprint
from rsa_blueprint import RSABlueprint
from sha_blueprint import SHABlueprint
from vigenerecipher_blueprint import VigenereCipherBlueprint

class ServerCore:

    def __init__(self):

        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log',
                                                  maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)

        self.app = Flask(__name__)
        self.app.add_url_rule("/", "index", self.index)

        self.loadBlueprints()

    def getApp(self):

        return self.app

    def loadBlueprints(self):

        """Each encryption method has its own blueprint. All the different
        blueprints must be loaded here"""

        allAlgos = {}
        historicalAlgos = {}
        outdatedAlgos = {}
        modernAlgos = {}
        hashingAlgos = {}

        self.aes = AESBlueprint()
        self.app.register_blueprint(self.aes)
        modernAlgos[self.aes.blueprintName] = self.aes.url
        self.logger.debug("Blueprint added: " + self.aes.blueprintName + ". Algorithm type: " + self.aes.algoType)

        self.blowfish = BlowfishBlueprint()
        self.app.register_blueprint(self.blowfish)
        modernAlgos[self.blowfish.blueprintName] = self.blowfish.url
        self.logger.debug("Blueprint added: " + self.blowfish.blueprintName + ". Algorithm type: " + self.blowfish.algoType)

        self.caesarCipher = CaesarCipherBlueprint()
        self.app.register_blueprint(self.caesarCipher)
        historicalAlgos[self.caesarCipher.blueprintName] = self.caesarCipher.url
        self.logger.debug("Blueprint added: " + self.caesarCipher.blueprintName + ". Algorithm type: " + self.caesarCipher.algoType)

        self.des = DESBlueprint()
        self.app.register_blueprint(self.des)
        outdatedAlgos[self.des.blueprintName] = self.des.url
        self.logger.debug("Blueprint added: " + self.des.blueprintName + ". Algorithm type: " + self.des.algoType)

        self.enigmaM3 = EnigmaM3Blueprint()
        self.app.register_blueprint(self.enigmaM3)
        historicalAlgos[self.enigmaM3.blueprintName] = self.enigmaM3.url
        self.logger.debug("Blueprint added: " + self.enigmaM3.blueprintName + ". Algorithm type: " + self.enigmaM3.algoType)

        self.md5 = MD5Blueprint()
        self.app.register_blueprint(self.md5)
        hashingAlgos[self.md5.blueprintName] = self.md5.url
        self.logger.debug("Blueprint added: " + self.md5.blueprintName + ". Algorithm type: " + self.md5.algoType)

        self.rsa = RSABlueprint()
        self.app.register_blueprint(self.rsa)
        modernAlgos[self.rsa.blueprintName] = self.rsa.url
        self.logger.debug("Blueprint added: " + self.rsa.blueprintName + ". Algorithm type: " + self.rsa.algoType)

        self.sha = SHABlueprint()
        self.app.register_blueprint(self.sha)
        hashingAlgos[self.sha.blueprintName] = self.sha.url
        self.logger.debug("Blueprint added: " + self.sha.blueprintName + ". Algorithm type: " + self.sha.algoType)

        self.vigenereCipher = VigenereCipherBlueprint()
        self.app.register_blueprint(self.vigenereCipher)
        historicalAlgos[self.vigenereCipher.blueprintName] = self.vigenereCipher.url
        self.logger.debug("Blueprint added: " + self.vigenereCipher.blueprintName + ". Algorithm type: " + self.vigenereCipher.algoType)


        allAlgos.update(historicalAlgos)
        allAlgos.update(outdatedAlgos)
        allAlgos.update(modernAlgos)
        allAlgos.update(hashingAlgos)


        allAlgosList = list(allAlgos.keys())
        allAlgosList.sort()
        historicalAlgosList = list(historicalAlgos.keys())
        historicalAlgosList.sort()
        outdatedAlgosList = list(outdatedAlgos.keys())
        outdatedAlgosList.sort()
        modernAlgosList = list(modernAlgos.keys())
        modernAlgosList.sort()
        hashingAlgosList = list(hashingAlgos.keys())
        hashingAlgosList.sort()

        # The code below gives to each blueprint a list of all the blueprints
        # (= encryption methods) available in the app, so that each blueprint can
        # load that list in the interface

        self.allAlgosSorted = []
        self.historicalAlgosSorted = []
        self.outdatedAlgosSorted = []
        self.modernAlgosSorted = []
        self.hashingAlgosSorted = []

        for i in allAlgosList: self.allAlgosSorted.append((i, allAlgos[i]))
        for i in historicalAlgosList: self.historicalAlgosSorted.append((i, historicalAlgos[i]))
        for i in outdatedAlgosList: self.outdatedAlgosSorted.append((i, outdatedAlgos[i]))
        for i in modernAlgosList: self.modernAlgosSorted.append((i, modernAlgos[i]))
        for i in hashingAlgosList: self.hashingAlgosSorted.append((i, hashingAlgos[i]))

        self.aes.setAlgosList([self.allAlgosSorted,
                               self.historicalAlgosSorted,
                               self.outdatedAlgosSorted,
                               self.modernAlgosSorted,
                               self.hashingAlgosSorted])

        self.blowfish.setAlgosList([self.allAlgosSorted,
                               self.historicalAlgosSorted,
                               self.outdatedAlgosSorted,
                               self.modernAlgosSorted,
                               self.hashingAlgosSorted])

        self.caesarCipher.setAlgosList([self.allAlgosSorted,
                               self.historicalAlgosSorted,
                               self.outdatedAlgosSorted,
                               self.modernAlgosSorted,
                               self.hashingAlgosSorted])

        self.des.setAlgosList([self.allAlgosSorted,
                               self.historicalAlgosSorted,
                               self.outdatedAlgosSorted,
                               self.modernAlgosSorted,
                               self.hashingAlgosSorted])

        self.enigmaM3.setAlgosList([self.allAlgosSorted,
                               self.historicalAlgosSorted,
                               self.outdatedAlgosSorted,
                               self.modernAlgosSorted,
                               self.hashingAlgosSorted])

        self.md5.setAlgosList([self.allAlgosSorted,
                               self.historicalAlgosSorted,
                               self.outdatedAlgosSorted,
                               self.modernAlgosSorted,
                               self.hashingAlgosSorted])

        self.rsa.setAlgosList([self.allAlgosSorted,
                               self.historicalAlgosSorted,
                               self.outdatedAlgosSorted,
                               self.modernAlgosSorted,
                               self.hashingAlgosSorted])

        self.sha.setAlgosList([self.allAlgosSorted,
                               self.historicalAlgosSorted,
                               self.outdatedAlgosSorted,
                               self.modernAlgosSorted,
                               self.hashingAlgosSorted])

        self.vigenereCipher.setAlgosList([self.allAlgosSorted,
                               self.historicalAlgosSorted,
                               self.outdatedAlgosSorted,
                               self.modernAlgosSorted,
                               self.hashingAlgosSorted])


    def launchServer(self):

        """This function is not intended for use in a production server!"""

        self.logger.info("Launching server")
        self.app.run(debug=True, threaded=True)

    def index(self):

        """This method is called when a request is sent to the homepage"""

        try:

            return render_template("index.html", allAlgos=self.allAlgosSorted,
                                   historicalAlgos=self.historicalAlgosSorted,
                                   outdatedAlgos=self.outdatedAlgosSorted,
                                   modernAlgos=self.modernAlgosSorted,
                                   hashingAlgos=self.hashingAlgosSorted)

        except TemplateNotFound:

            abort(404)
