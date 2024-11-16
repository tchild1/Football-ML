import pandas as pd
import csv
from dataStructures.Game import Game
from utils.utils import gameToDictionary
import os
from tqdm import tqdm


print('reading data')
df = pd.read_csv('./playByPlayData/compiledPlayByPlayData.csv')

print('compiling data')

gamesDictionary: dict[int: Game] = {}
pbar = tqdm(total=len(df))
df.fillna('', inplace=True)

for row in df.itertuples():
    # if row.GameId == 2019092909:
    #     breakpoint()
    if row.GameId in gamesDictionary:
        game: Game = gamesDictionary[row.GameId]
        game.processSinglePlay(row)
    else:
        gamesDictionary[row.GameId] = Game(row.GameId, row.OffenseTeam, row.DefenseTeam)
        game: Game = gamesDictionary[row.GameId]
        game.processSinglePlay(row)
    pbar.update(1)


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
