import pandas as pd
import os
from tqdm import tqdm

dfs = []

path = './playByPlayData'
for filename in os.listdir(path):
    if filename == 'compiledPlayByPlayData.csv':
        continue
    filePath = os.path.join(path, filename)
    
    if os.path.isfile(filePath):
        newDf = pd.read_csv(filePath)
        newDf.fillna('', inplace=True)

        dfs.append(newDf)


# go through the data and check for missing OffenseTeam and DefenseTeam
# if the offense AND defense team are missing then remove the row
# if only one is missing, find another row with the same GameId and fill in the missing team
for df in dfs:
    pbar = tqdm(total=len(df))
    unique_game_ids = df.GameId.unique()
    game_name_pairs = {}
    for row in df.itertuples():
        if row.OffenseTeam == '' and row.DefenseTeam == '':
            df.drop(row.Index, inplace=True)
        elif row.OffenseTeam == '':
            if row.GameId in game_name_pairs:
                # pick the team name that is not the same as the defense team
                if row.DefenseTeam == game_name_pairs[row.GameId][0]:
                    df.at[row.Index, 'OffenseTeam'] = game_name_pairs[row.GameId][1]
                else:
                    df.at[row.Index, 'OffenseTeam'] = game_name_pairs[row.GameId][0]
            else:
                otherRow = df.loc[(df.GameId == row.GameId) & (df.DefenseTeam != '') & (df.OffenseTeam != '')].iloc[0]
                otherDefenseTeam = otherRow.DefenseTeam
                otherOffenseTeam = otherRow.OffenseTeam
                if row.DefenseTeam == otherDefenseTeam:
                    df.at[row.Index, 'OffenseTeam'] = otherOffenseTeam
                else:
                    df.at[row.Index, 'OffenseTeam'] = otherDefenseTeam
        elif row.DefenseTeam == '':
            if row.GameId in game_name_pairs:
                # pick the team name that is not the same as the offense team
                if row.OffenseTeam == game_name_pairs[row.GameId][0]:
                    df.at[row.Index, 'DefenseTeam'] = game_name_pairs[row.GameId][1]
                else:
                    df.at[row.Index, 'DefenseTeam'] = game_name_pairs[row.GameId][0]
            else:
                otherRow = df.loc[(df.GameId == row.GameId) & (df.DefenseTeam != '') & (df.OffenseTeam != '')].iloc[0]
                otherDefenseTeam = otherRow.DefenseTeam
                otherOffenseTeam = otherRow.OffenseTeam
                if row.OffenseTeam == otherOffenseTeam:
                    df.at[row.Index, 'DefenseTeam'] = otherDefenseTeam
                else:
                    df.at[row.Index, 'DefenseTeam'] = otherOffenseTeam
        elif row.GameId not in game_name_pairs:
            game_name_pairs[row.GameId] = [row.OffenseTeam, row.DefenseTeam]
        pbar.update(1)

# save the cleaned data
df = pd.concat(dfs, ignore_index=True)
df.fillna('', inplace=True)
df.to_csv('playByPlayData/compiledPlayByPlayData.csv', index=False)