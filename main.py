import json
from GameQuake import GameQuake

filename = 'Quake.txt'
gameAmount = GameQuake(filename, 0).gameAmount()
answerList = []
for c in range(1, gameAmount + 1):
    answerList.append(GameQuake(filename, c).dictFinal)

outfile = open("Parser.json", "w")
json.dump(answerList, outfile, indent=4, sort_keys=False)

