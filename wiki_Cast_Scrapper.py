#!/usr/bin/python3
#Scraping wikipedia page to fetch the list of cast members(actor name) and their character names via command line input
## USAGE
# pyhton wiki_Cast_Scrapper.py <EXACT MOVIE NAME FROM WIKIPEDIA>
import sys
import requests
import bs4
import pandas as pd
from bs4 import BeautifulSoup

import requests

movie_name = sys.argv[1:] # get the movie name as input from the comand line

website_url = requests.get('https://en.wikipedia.org/wiki/' + ' '.join(movie_name)).text

soup = BeautifulSoup(website_url,'lxml')

elements = soup.find_all('h2')
for element in elements:
	if element.find_all(id='Cast'):
		Cast_data = element.find_next_sibling()
		if Cast_data.find_all('img'):
			Cast_data = Cast_data.find_next_sibling()
		break

links = Cast_data.findAll('li')
# Print all the cast info Gathered
full_texts = []
for link in links:
	full_texts.append(link.get_text())
for text in full_texts:
	print(text +'\n')

cast_members = []
character_names = []

# Split the Sting into cast member's name and the character they played in the movie
for text in full_texts:
	new_string = text
	if text.split(':'):
		temp1_string = text.split(':')
		new_string = temp1_string[0]
	temp = new_string.split("as")
	cast_members.append(temp[0])
	character_names.append(temp[1])

# Print the names of cat members and character names in the form of lists
print(cast_members)
print(character_names)

### final answer in the form of an pandas database

# df = pd.DataFrame()
# df['Cast_members'] = cast_members
# df['Character_names'] = character_names

# print(df)