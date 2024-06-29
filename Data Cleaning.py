import pandas as pd
import numpy as np
import os
df_UEFA_missing_data = pd.read_csv('UEFA_missing_data.csv')
df_UEFA = pd.read_csv('UEFA_last_10_year_matches.csv')
df_fixtures = pd.read_csv('UEFA_Euro_2024_fixture.csv')
os.getcwd()
os.chdir(r'C:\Users\Ananya\AppData\Roaming\JetBrains\PyCharm2024.1\scratches')
df_fixtures['home'] = df_fixtures['home'].str.strip()
df_fixtures['away'] = df_fixtures['away'].str.strip()
df_UEFA_missing_data[df_UEFA_missing_data['home'].isnull()].dropna()
df_UEFA_missing_data[df_UEFA_missing_data['away'].isnull()].dropna()
df_UEFA_missing_data.dropna(inplace=True)
df_UEFA[df_UEFA['home'].isnull()].dropna()
df_UEFA[df_UEFA['away'].isnull()].dropna()

df_UEFA = pd.concat([df_UEFA, df_UEFA_missing_data], ignore_index=True)
df_UEFA.drop_duplicates(inplace=True)
df_UEFA.sort_values('Tournament', inplace=True)
df_UEFA = df_UEFA.replace(to_replace='None', value=np.nan).dropna()

df_UEFA['score'] = df_UEFA[r'score'].str.replace('[^\\d–]', '', regex=True)
df_UEFA['home'] = df_UEFA[r'home'].str.strip()
df_UEFA['away'] = df_UEFA[r'away'].str.strip()
df_UEFA[['HomeGoals', 'AwayGoals']]=df_UEFA[r'score'].str.split('–', expand = True)
df_UEFA.drop('score', axis=1, inplace=True)
df_UEFA['AwayGoals'] = df_UEFA['AwayGoals'].replace(to_replace='None', value=np.nan).dropna()
df_UEFA.dropna(inplace=True)

df_UEFA[['HomeGoals']] = df_UEFA[['HomeGoals']].astype(int)
df_UEFA[['AwayGoals']] = df_UEFA[['AwayGoals']].astype(int)

df_UEFA['TotalGoals'] = df_UEFA['HomeGoals'] + df_UEFA['AwayGoals']

df_UEFA.to_csv('clean_UEFA_last_10_year_matches.csv', index = False)
df_fixtures.to_csv('clean_UEFA_Euro_2024_fixture.csv', index = False)