from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

Tournaments = ['UEFA_Euro_2024', 'UEFA_Euro_2016', 'UEFA_Euro_2012', 'UEFA_Euro_2020', '2010_FIFA_World_Cup', '2014_FIFA_World_Cup', '2018_FIFA_World_Cup', '2022_FIFA_World_Cup', '2022–23_UEFA_Nations_League_C', '2018–19_UEFA_Nations_League_B',
'2022_FIFA_World_Cup_qualification_–_UEFA_Group_C', '2022_FIFA_World_Cup_qualification_–_UEFA_Group_E', '2022_FIFA_World_Cup_qualification_–_UEFA_Group_F', '2022_FIFA_World_Cup_qualification_–_UEFA_Group_G', '2022_FIFA_World_Cup_qualification_–_UEFA_Group_H', '2022_FIFA_World_Cup_qualification_–_UEFA_Group_I',
'2022_FIFA_World_Cup_qualification_–_UEFA_Group_I', '2018_FIFA_World_Cup_qualification_–_UEFA_Group_A', '2018_FIFA_World_Cup_qualification_–_UEFA_Group_B', '2018_FIFA_World_Cup_qualification_–_UEFA_Group_C', '2018_FIFA_World_Cup_qualification_–_UEFA_Group_D', '2018_FIFA_World_Cup_qualification_–_UEFA_Group_E',
'2018_FIFA_World_Cup_qualification_–_UEFA_Group_F', '2018_FIFA_World_Cup_qualification_–_UEFA_Group_G', '2018_FIFA_World_Cup_qualification_–_UEFA_Group_H', '2018_FIFA_World_Cup_qualification_–_UEFA_Group_I',
'UEFA_Euro_2020_qualifying_Group_A', 'UEFA_Euro_2020_qualifying_Group_B', 'UEFA_Euro_2020_qualifying_Group_B', 'UEFA_Euro_2020_qualifying_Group_D', 'UEFA_Euro_2020_qualifying_Group_E', 'UEFA_Euro_2020_qualifying_Group_F', 'UEFA_Euro_2020_qualifying_Group_G', 'UEFA_Euro_2020_qualifying_Group_H', 'UEFA_Euro_2020_qualifying_Group_I', 'UEFA_Euro_2020_qualifying_Group_J',
'UEFA_Euro_2024_qualifying_Group_A', 'UEFA_Euro_2024_qualifying_Group_B', 'UEFA_Euro_2024_qualifying_Group_C', 'UEFA_Euro_2024_qualifying_Group_D', 'UEFA_Euro_2024_qualifying_Group_E', 'UEFA_Euro_2024_qualifying_Group_F', 'UEFA_Euro_2024_qualifying_Group_G', 'UEFA_Euro_2024_qualifying_Group_H', 'UEFA_Euro_2024_qualifying_Group_I', 'UEFA_Euro_2024_qualifying_Group_J',
'2018–19_UEFA_Nations_League_A', '2018–19_UEFA_Nations_League_C', '2020–21_UEFA_Nations_League_A', '2020–21_UEFA_Nations_League_B', '2020–21_UEFA_Nations_League_C', '2022–23_UEFA_Nations_League_A', '2022–23_UEFA_Nations_League_B',
'2022_FIFA_World_Cup_qualification_–_UEFA_Group_A', '2022_FIFA_World_Cup_qualification_–_UEFA_Group_B', '2022_FIFA_World_Cup_qualification_–_UEFA_Group_D']


def get_missing_data(tournament):
    web = f'https://en.wikipedia.org/wiki/{tournament}'

    driver.get(web)
    matches = driver.find_elements(by='xpath', value='//td[@align="right"]/.. | //td[@style="text-align:right;"]/..')
    # matches = driver.find_elements(by='xpath', value='//tr[@style="font-size:90%"]')

    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find_element(by='xpath', value='./td[1]').text)
        score.append(match.find_element(by='xpath', value='./td[2]').text)
        away.append(match.find_element(by='xpath', value='./td[3]').text)

    dict_football = {'home': home, 'score': score, 'away': away}
    df_football = pd.DataFrame(dict_football)
    df_football['Tournament'] = tournament
    time.sleep(2)
    return df_football


UEFA_missing_data = [get_missing_data(Tournament) for Tournament in Tournaments]
driver.quit()
UEFA_missing_data = pd.concat(UEFA_missing_data, ignore_index=True)
UEFA_missing_data.to_csv("UEFA_missing_data.csv", index=False)
