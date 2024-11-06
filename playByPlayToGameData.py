import pandas as pd
import csv
from dataStructures.Game import Game
from utils.utils import gameToDictionary
import os


print('reading data')

df = pd.DataFrame()

path = './playByPlayData'
for filename in os.listdir(path):
    filePath = os.path.join(path, filename)
    
    if os.path.isfile(filePath):
        newDf = pd.read_csv(filePath)
        newDf.fillna('', inplace=True)

        df = pd.concat([df, newDf], ignore_index=True)


print('compiling data')

gamesDictionary: dict[int: Game] = {}

for row in df.itertuples():
    if row.GameId in gamesDictionary:
        game: Game = gamesDictionary[row.GameId]
        game.processSinglePlay(row)
    else:
        gamesDictionary[row.GameId] = Game(row.GameId, row.OffenseTeam, row.DefenseTeam)
        game: Game = gamesDictionary[row.GameId]
        game.processSinglePlay(row)


print('converting game data to a df')
allData = []
for game in gamesDictionary:
    allData.extend(gameToDictionary(gamesDictionary[game]))


print('getting fieldnames')
fieldNames = set()
for row in allData:
    fieldNames.update(row.keys())

fieldNames = sorted(fieldNames)


print('writing to csv')
with open('./compiledData/compliedData.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldNames)
    writer.writeheader()
    writer.writerows(allData)
