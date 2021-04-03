import requests
from bs4 import BeautifulSoup
from datetime import date

def get_linchpin():
	response = requests.get('https://www.crossfitlinchpin.com/')

	soup = BeautifulSoup(response.content,'html.parser')

	div = soup.find('div',{'class':'featured-wods'})

	p = div.find_all('p')[2]

	spans = p.find_all('span')

	wod = ''

	for span in spans:
		wod += span.text + '\n'

	data = {
		'name' : 'Crossfit Linchpin',
		'link' : 'https://www.crossfitlinchpin.com/',
		'wod' : wod,
		'date' : date.today()
	}
	return data