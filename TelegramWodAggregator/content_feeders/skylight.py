import requests
from bs4 import BeautifulSoup
from datetime import date

def get_skylight():
	response = requests.get('http://crossfitskylight.com/wod/')

	soup = BeautifulSoup(response.content,'html.parser')

	div = soup.find('div',{'class':'entry-content'})

	ps = div.find_all('p')[2:]

	wod = ''

	for p in ps:
		wod += p.text + '\n'

	data = {
		'name':'Corssfit Skylight',
		'link':'http://crossfitskylight.com/wod/',
		'wod' : wod,
		'date' : date.today()
	}

	return data