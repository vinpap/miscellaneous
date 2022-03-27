import logging
import logging.handlers

from flask import render_template, abort, request
from jinja2 import TemplateNotFound

from baseblueprint import BaseBlueprint
from caesarcipher_algo import CaesarCipher

"""The class below is a blueprint loaded by Flask. See baseblueprint.py for
more info"""

class CaesarCipherBlueprint(BaseBlueprint):
    
    def __init__(self):
        
        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log', 
                                                  maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)
        
        self.algo = CaesarCipher()
        
        url = "/caesarcipher"
        super().__init__('Caesar Cipher', 'HISTORICAL', url)
        
        self.add_url_rule(url, "caesarcipher", self.caesarCipher)
        self.add_url_rule(url + "/encryption", "caesar_cipher_encryption", self.displayEncryptedText, methods=["POST"])
        self.add_url_rule(url + "/decryption", "caesar_cipher_decryption", self.displayDecryptedText, methods=["POST"])
        
    
    def caesarCipher(self):
        
        """This method is called when a request is sent to /caesarcipher"""
        
        try:
            
            return render_template("caesarcipher.html", 
                                   mode="homepage",
                                   allAlgos=self._allAlgosSorted, 
                                   historicalAlgos=self._historicalAlgosSorted, 
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)
        
        except TemplateNotFound:
            
            abort(404)
    

    def displayEncryptedText(self):
        
        """This method is called when a request is sent to /caesarcipher/encryption"""
        
        message = request.form["message"]
        key = request.form["key_area"]
        
        
        try:
            
            key = int(key)
            
        except ValueError:
            
            errorMsg = ("This key is not valid. The key must be an integer")
            
            try:

                return render_template("caesarcipher.html",
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

            return render_template("caesarcipher.html",
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
        
        """This method is called when a request is sent to /caesarcipher/decryption"""
        
        message = request.form["message"]
        key = request.form["key_area"]
        
        try:
            
            key = int(key)
            
        except ValueError:
            
            errorMsg = ("This key is not valid. The key must be an integer")
            
            try:

                return render_template("caesarcipher.html",
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

            return render_template("caesarcipher.html", 
                                   mode="displayDecryptedText",
                                   decryptedMessage=decryptedText,
                                   allAlgos=self._allAlgosSorted, 
                                   historicalAlgos=self._historicalAlgosSorted, 
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)
        
        except TemplateNotFound:
            
            abort(404)