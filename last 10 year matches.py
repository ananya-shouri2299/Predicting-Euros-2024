from bs4 import BeautifulSoup
import requests
import pandas as pd
Tournaments = ['UEFA_Euro_2024', 'UEFA_Euro_2016', 'UEFA_Euro_2012', 'UEFA_Euro_2020', '2010_FIFA_World_Cup', '2014_FIFA_World_Cup', '2018_FIFA_World_Cup', '2022_FIFA_World_Cup', '2022–23_UEFA_Nations_League_C', '2018–19_UEFA_Nations_League_B',
'2022_FIFA_World_Cup_qualification_–_UEFA_Group_C', '2022_FIFA_World_Cup_qualification_–_UEFA_Group_E', '2022_FIFA_World_Cup_qualification_–_UEFA_Group_F', '2022_FIFA_World_Cup_qualification_–_UEFA_Group_G', '2022_FIFA_World_Cup_qualification_–_UEFA_Group_H', '2022_FIFA_World_Cup_qualification_–_UEFA_Group_I',
'2022_FIFA_World_Cup_qualification_–_UEFA_Group_I', '2018_FIFA_World_Cup_qualification_–_UEFA_Group_A', '2018_FIFA_World_Cup_qualification_–_UEFA_Group_B', '2018_FIFA_World_Cup_qualification_–_UEFA_Group_C', '2018_FIFA_World_Cup_qualification_–_UEFA_Group_D', '2018_FIFA_World_Cup_qualification_–_UEFA_Group_E',
'2018_FIFA_World_Cup_qualification_–_UEFA_Group_F', '2018_FIFA_World_Cup_qualification_–_UEFA_Group_G', '2018_FIFA_World_Cup_qualification_–_UEFA_Group_H', '2018_FIFA_World_Cup_qualification_–_UEFA_Group_I',
'UEFA_Euro_2020_qualifying_Group_A', 'UEFA_Euro_2020_qualifying_Group_B', 'UEFA_Euro_2020_qualifying_Group_B', 'UEFA_Euro_2020_qualifying_Group_D', 'UEFA_Euro_2020_qualifying_Group_E', 'UEFA_Euro_2020_qualifying_Group_F', 'UEFA_Euro_2020_qualifying_Group_G', 'UEFA_Euro_2020_qualifying_Group_H', 'UEFA_Euro_2020_qualifying_Group_I', 'UEFA_Euro_2020_qualifying_Group_J',
'UEFA_Euro_2024_qualifying_Group_A', 'UEFA_Euro_2024_qualifying_Group_B', 'UEFA_Euro_2024_qualifying_Group_C', 'UEFA_Euro_2024_qualifying_Group_D', 'UEFA_Euro_2024_qualifying_Group_E', 'UEFA_Euro_2024_qualifying_Group_F', 'UEFA_Euro_2024_qualifying_Group_G', 'UEFA_Euro_2024_qualifying_Group_H', 'UEFA_Euro_2024_qualifying_Group_I', 'UEFA_Euro_2024_qualifying_Group_J',
'2018–19_UEFA_Nations_League_A', '2018–19_UEFA_Nations_League_C', '2020–21_UEFA_Nations_League_A', '2020–21_UEFA_Nations_League_B', '2020–21_UEFA_Nations_League_C', '2022–23_UEFA_Nations_League_A', '2022–23_UEFA_Nations_League_B',
'2022_FIFA_World_Cup_qualification_–_UEFA_Group_A', '2022_FIFA_World_Cup_qualification_–_UEFA_Group_B', '2022_FIFA_World_Cup_qualification_–_UEFA_Group_D']

def get_matches(Tournament):
  web =f'https://en.wikipedia.org/wiki/{Tournament}'
  response = requests.get(web)
  content = response.text
  soup = BeautifulSoup(content, 'lxml')

  matches = soup.find_all('div', class_='footballbox')

  home =[]
  score = []
  away = []

  for match in matches:
    home.append(match.find('th', class_= 'fhome').get_text())
    score.append(match.find('th', class_= 'fscore').get_text())
    away.append(match.find('th', class_= 'faway').get_text())

  dict_football = {'home' : home, 'score' : score, 'away' : away}
  df_football = pd.DataFrame(dict_football)
  df_football['Tournament'] = Tournament
  return df_football

UEFA = [get_matches(Tournament) for Tournament in Tournaments]
df_UEFA = pd.concat(UEFA, ignore_index=True)
df_UEFA.to_csv('UEFA_last_10_year_matches.csv', index=False)

df_fixture = get_matches('UEFA_Euro_2024')
df_fixture.to_csv('UEFA_Euro_2024_fixture.csv', index=False)