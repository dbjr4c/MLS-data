#--Web scraping packages
from bs4 import BeautifulSoup
import requests
#Pandas/numpy for data manipulation
import pandas as pd
import numpy as np

BASE_URL = ['https://www.mlssoccer.com/stats/season', ]

teams = []

for t in BASE_URL:
	html = requests.get(t).text
	soup = BeautifulSoup(html, "html.parser")

	stats_table = soup.find('table')
	# print(stats_table)

	try:

		for row in stats_table.find_all('tr'):
			cell = row.find_all('td')
			    
			for cell in cells:
        			data.append(cell.text.encode('utf-8'))

			writer.writerow(data)