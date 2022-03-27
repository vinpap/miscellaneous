import logging
import logging.handlers

from flask import render_template, abort, request
from jinja2 import TemplateNotFound

from baseblueprint import BaseBlueprint
from des_algo import DES

"""The class below is a blueprint loaded by Flask. See baseblueprint.py for
more info"""

class DESBlueprint(BaseBlueprint):
    
    def __init__(self):
        
        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log', 
                                                  maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)
        
        self.algo = DES()
        
        url = "/des"
        super().__init__('DES', 'OUTDATED', url)
        
        self.add_url_rule(url, "des", self.DES)
        self.add_url_rule(url + "/encryption", "des_encryption", self.displayEncryptedText, methods=["POST"])
        self.add_url_rule(url + "/decryption", "des_decryption", self.displayDecryptedText, methods=["POST"])
        
    
    def DES(self):
        
        """This method is called when a request is sent to /des"""
        
        try:
            
            return render_template("des.html", 
                                   mode="homepage",
                                   allAlgos=self._allAlgosSorted, 
                                   historicalAlgos=self._historicalAlgosSorted, 
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)        
        except TemplateNotFound:
            
            abort(404)
    

    def displayEncryptedText(self):
        
        """This method is called when a request is sent to /des/encryption"""
        
        message = request.form["message"]
        key = request.form["key_area"]
        
        
        if len(bytes(key, encoding='utf-8')) not in (8, 16, 24):
            
            errorMsg = ("This key is not valid. Please enter a key of 64, "
                        "128 or 192 bits. This amounts to 8, 16 or 24 "
                        "characters in ASCII")
            try:

                return render_template("des.html",
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

            return render_template("des.html",
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
        
        """This method is called when a request is sent to /des/decryption"""
        
        message = request.form["message"]
        key = request.form["key_area"]
        
        if len(bytes(key, encoding='utf-8')) not in (8, 16, 24):
            
            errorMsg = ("This key is not valid. Please enter a key of 64, "
                        "128 or 192 bits. This amounts to 8, 16 or 24 "
                        "characters in ASCII")
            try:

                return render_template("des.html",
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
        
        if decryptedText == 0: # Value returned when the key is wrong
            
            errorMsg =("Error during the decryption of the message. Please make"
                       " sure you are using a valid key")
            
            try:
                
                return render_template("des.html",
                                   mode="decryptionError",
                                   error=errorMsg,
                                   allAlgos=self._allAlgosSorted, 
                                   historicalAlgos=self._historicalAlgosSorted, 
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)
            
            except TemplateNotFound:
            
                abort(404)
        
        elif decryptedText == 1: # Value returned when the encrypted text is not in hexa
            
            errorMsg =("Error during the decryption of the message. Please make"
                       " sure the message you want to decrypt is encoded in"
                       " hexadecimal")
            
            try:
                
                return render_template("des.html",
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

            return render_template("des.html", 
                                   mode="displayDecryptedText",
                                   decryptedMessage=decryptedText,
                                   allAlgos=self._allAlgosSorted, 
                                   historicalAlgos=self._historicalAlgosSorted, 
                                   outdatedAlgos=self._outdatedAlgosSorted,
                                   modernAlgos=self._modernAlgosSorted,
                                   hashingAlgos=self._hashingAlgosSorted)
        
        except TemplateNotFound:
            
            abort(404)
   