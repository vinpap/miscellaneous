import logging
import logging.handlers

from flask import Blueprint


"""This module defines the class BaseBlueprint, the parent class for all the
blueprints loaded by Flask. Each encryption/hashing method in the app has its
own blueprint.
This approach allows for more modularity, as new encryption methods can be added
in the app without the need for significant changes in the code. You just need to
create a module containing a class derivating from BaseBlueprint."""

class BaseBlueprint(Blueprint):

    def __init__(self, blueprintName, algoType, url):

        self.logger = logging.getLogger(__name__)
        fh = logging.handlers.RotatingFileHandler('logs/' + __name__ + '.log',
                                                  maxBytes=10000000, backupCount=100)
        fh.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s'))
        self.logger.addHandler(fh)

        super().__init__(blueprintName, __name__)
        self._blueprintName = blueprintName
        self._algoType = algoType
        self._url = url

        self._allAlgosSorted = []
        self._historicalAlgosSorted = []
        self._outdatedAlgosSorted = []
        self._modernAlgosSorted = []
        self._hashingAlgosSorted = []

    def setAlgosList(self, algosList):

        self._allAlgosSorted = algosList[0]
        self._historicalAlgosSorted = algosList[1]
        self._outdatedAlgosSorted = algosList[2]
        self._modernAlgosSorted = algosList[3]
        self._hashingAlgosSorted = algosList[4]

    @property
    def blueprintName(self):

        return self._blueprintName

    @blueprintName.setter
    def blueprintName(self, newName):

        self.logger.error("Error during the modification of blueprint object " + self.__blueprintName + " : the name of the blueprint cannot be changed from outside the blueprint class")


    @property
    def algoType(self):

        return self._algoType

    @algoType.setter
    def algoType(self, newAlgoType):

        self.logger.error("Error during the modification of blueprint object " + self.__blueprintName + " : the type of the blueprint's algorithm cannot be changed from outside the blueprint class")


    @property
    def url(self):

        return self._url

    @url.setter
    def url(self, newURL):

        self.logger.error("Error during the modification of blueprint object " + self.__blueprintName + " : blueprint URL cannot be changed from outside the blueprint class")

    @property
    def allAlgosSorted(self):

        return self._allAlgosSorted

    @allAlgosSorted.setter
    def allAlgosSorted(self):

        self.logger.error("Error during the modification of blueprint object " + self.__blueprintName + " : the algorithms list cannot be changed from outside the blueprint class")

    @property
    def historicalAlgosSorted(self):

        return self._historicalAlgosSorted

    @historicalAlgosSorted.setter
    def historicalAlgosSorted(self):

        self.logger.error("Error during the modification of blueprint object " + self.__blueprintName + " : the algorithms list cannot be changed from outside the blueprint class")

    @property
    def outdatedAlgosSorted(self):

        return self._outdatedAlgosSorted

    @outdatedAlgosSorted.setter
    def outdatedAlgosSorted(self):

        self.logger.error("Error during the modification of blueprint object " + self.__blueprintName + " : the algorithms list cannot be changed from outside the blueprint class")

    @property
    def modernAlgosSorted(self):

        return self._modernAlgosSorted

    @modernAlgosSorted.setter
    def modernAlgosSorted(self):

        self.logger.error("Error during the modification of blueprint object " + self.__blueprintName + " : the algorithms list cannot be changed from outside the blueprint class")

    @property
    def hashingAlgosSorted(self):

        return self._hashingAlgosSorted

    @hashingAlgosSorted.setter
    def hashingAlgosSorted(self):

        self.logger.error("Error during the modification of blueprint object " + self.__blueprintName + " : the algorithms list cannot be changed from outside the blueprint class")