from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas as pd

driver_path = "./chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path

browser = webdriver.Chrome(executable_path=driver_path, options=option)

bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(bright_stars_url)
print(page)

soup = BeautifulSoup(page.text, 'html.parser')

star_table = soup.find('table')

temp_list = []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)


Star_names = []
Distance = []
Mass = []
Radius = []
Lum = []

for i in range(1, len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])

df2 = pd.DataFrame(list(zip(Star_names, Distance, Mass, Radius)), columns=[
                   'Star_name', 'Distance', 'Mass', 'Radius'])
print(df2)


df2.to_csv('star_data.csv')
