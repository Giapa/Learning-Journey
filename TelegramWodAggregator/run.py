import telegram
from config import get_token
from content_feeders.linchpin import get_linchpin
from content_feeders.skylight import get_skylight

bot = telegram.Bot(token=get_token())

def send_wods():
	datas = []
	datas.append(get_linchpin())
	datas.append(get_skylight())
	for data in datas:
		msg = f'{data["date"]} \nFrom: {data["name"]} \n\nWod: {data["wod"]} \n<a href="{data["link"]}">source</a>'
		bot.send_message(chat_id='@cwods',text=msg , parse_mode=telegram.ParseMode.HTML)
		print(f'Wod from {data["name"]} is uploaded')

if __name__ == '__main__':
	send_wods()