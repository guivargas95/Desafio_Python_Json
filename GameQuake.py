class GameQuake:
    def __init__(self, gameFile, gameNumber):
        self.__dictFinal = {}
        self.__gameFile = gameFile
        self.__gameNumber = gameNumber
        self.openFile(self.__gameFile, self.__gameNumber)


    def openFile(self, file, gameNumber):
        '''Abre o arquivo e separa o jogo especificado'''
        cont = 0
        gameLines = []
        with open(file) as fh:
            for line in fh:
                if "InitGame:" in line:
                    cont += 1
                if cont == gameNumber:
                    gameLines.append(line)
        self.playerList(gameLines)

    def playerList(self, gameLines):
        '''Cria a lista de jogadores com alterações de nome'''
        playersDict = {}
        playersList = []
        for c,line in enumerate(gameLines):
            if 'ClientUserinfoChanged:' in line:
                playerId = int(line.split()[2]) - 1
                playerName = line.split("\\")[1]
                if len(playersList) == 0:
                    playersDict.update({c: {}})
                    playersDict[c]['id'] = playerId
                    playersDict[c]['name'] = playerName
                    playersDict[c]['kills'] = 0
                    playersDict[c]['old_names'] = []
                    playersList.append(playersDict[c])
                else:
                    for each, player in enumerate(playersList):
                        if player['id'] == playerId and player['name'] != playerName:
                            player['old_names'].append(player['name'])
                            player['name'] = playerName
                            break
                        elif player['id'] == playerId and player['name'] == playerName:
                            break
                        elif player['id'] != playerId and len(playersList) - 1 == each:
                            playersDict.update({c: {}})
                            playersDict[c]['id'] = playerId
                            playersDict[c]['name'] = playerName
                            playersDict[c]['kills'] = 0
                            playersDict[c]['old_names'] = []
                            playersList.append(playersDict[c])
        self.kills(gameLines, playersList)

    def kills(self, gameLines, playersList):
        '''Faz a contagem de kills da partida e dos players'''
        gameTotalKills = 0
        for line in gameLines:
            if "Kill:" in line:
                gameTotalKills += 1
                if int(line.split()[2]) == 1022 or int(line.split()[2]) == int(line.split()[3]):
                    for player in playersList:
                        if player['id'] == int(line.split()[3]):
                            player['kills'] -= 1
                elif int(line.split()[2]) != 1022 and int(line.split()[2]) != int(line.split()[3]):
                    for player in playersList:
                        if player['id'] == int(line.split()[2]):
                            player['kills'] += 1
        self.__dictFinal = {"game": self.__gameNumber, "status": {"total_kills": gameTotalKills, "players": playersList}}.copy()

    def gameAmount(self):
        '''Verifica a quantidade de partidas dentro do arquivo txt do game'''
        quant = 0
        with open(self.__gameFile) as fh:
            for line in fh:
                if "InitGame:" in line:
                    quant += 1
        return quant

    @property
    def dictFinal(self):
        '''Devolve o dict final'''
        return self.__dictFinal






