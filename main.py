import json
from GameQuake import GameQuake

filename = 'Quake.txt'
gameQuant = 0
listaTotal = []
for c in range(1,23):
    listaTotal.append(GameQuake(filename, c).dictFinal)

outfile = open("teste1.json", "w")
json.dump(listaTotal, outfile, indent=4, sort_keys=False)

