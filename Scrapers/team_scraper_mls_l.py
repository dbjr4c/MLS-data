#--Web scraping packages
from bs4 import BeautifulSoup
import requests
#Pandas/numpy for data manipulation
import pandas as pd
import numpy as np

BASE_URL = ['https://www.mlssoccer.com/stats/team', ]

teams = []

for t in BASE_URL:
	html = requests.get(t).text
	soup = BeautifulSoup(html, "html.parser")

	stats_table = soup.find('table')
	# print(stats_table)

	try:

		for row in stats_table.find_all('tr'):
			cols = row.find_all('td')
			if len(cols) == 12:
				teams.append((cols[0].text.strip(), cols[1].text.strip(), cols[2].text.strip(), cols[3].text.strip(), cols[4].text.strip(), cols[5].text.strip(), cols[6].text.strip(), cols[7].text.strip(), cols[8].text.strip(), cols[9].text.strip(), cols[10].text.strip(), cols[11].text.strip()))

	except: pass

team_array = np.asarray(teams)
len(team_array)

df = pd.DataFrame(team_array)

df.columns = ['Club', 'GP', 'G', 'A', 'SHTS', 'SOG', 'FC', 'FS', 'OFF', 'CK', 'PKG', 'PKA']
#df.head(10)

df.to_csv('July_teams.csv')
