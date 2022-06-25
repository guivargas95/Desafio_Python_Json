class GameQuake:
    def __init__(self, gameFile, gameNumber):
        self.__gameFile = gameFile
        self.__gameNumber = gameNumber
        self.openFile(self.__gameFile, self.__gameNumber)
        self.__gameLines = []
        self.__playerList = []
        self.__killList = []


    def openFile(self, file, gameNumber):
        pass