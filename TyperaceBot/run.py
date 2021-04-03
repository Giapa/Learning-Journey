from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from time import sleep
from initialize import initialize
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import uniform

def start(driver, link='https://play.typeracer.com/'):

    print('---- Joining random game')

    try:
        if link == 'https://play.typeracer.com/':

            driver.get(link)

            sleep(4)

            accept_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/button[2]')

            accept_button.click()

            while True:
                if 'Enter a typing race' in driver.page_source:
                    break

            element = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL, Keys.ALT, 'I')

        else:

            driver.get(link)

            sleep(2)

            accept_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/button[2]')

            accept_button.click()

            sleep(3)

            element = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL, Keys.ALT, 'K')


        print('---- Went in a game')

        sleep(2)

        text = ""

        source = driver.page_source
        soup = BeautifulSoup(source,'html.parser')
        table = soup.find('table',{'class':'inputPanel'})
        next_table = table.find('table')
        div = next_table.find('div')
        spans = div.find_all('span')
        for span in spans:
            text = text + span.text

        print(f'---- Text is: "{text}" and length:{len(text)}')

        WebDriverWait(driver,2000).until(EC.element_to_be_clickable((By.CLASS_NAME,'txtInput')))

        input_field = driver.find_element_by_class_name('txtInput')
        if len(text) <= 120:
            end = 3
            step = 3
            new_text = text[12:]
            sleeping_time = 0.11
            print(f'---- Microscopic text. Step:{step}')
        elif len(text) <= 150:
            end = 4
            step = 4
            new_text = text[16:]
            sleeping_time = 0.111
            print(f'---- Tiny text. Step:{step}')
        elif len(text) <= 170:
            end = 4
            step = 4
            new_text = text[16:]
            sleeping_time = 0.112
            print(f'---- Super small text. Step:{step}')
        elif len(text) <= 200:
            end = 4
            step = 4
            new_text = text[16:]
            sleeping_time = 0.109
            print(f'---- Small text. Step:{step}')
        elif len(text) <= 240:
            end = 4
            step = 4
            new_text = text[16:]
            sleeping_time = 0.1093
            print(f'---- Medium text. Step:{step}')
        elif len(text) <= 270:
            end = 5
            step = 5
            new_text = text[20:]
            sleeping_time = 0.10925
            print(f'---- Big text. Step:{step}')
        else:
            end = 5
            step = 5
            new_text = text[20:]
            sleeping_time = 0.1088
            print(f'---- Huge text. Step:{step}')
        start = 0
        for i in range(4):
            inp = text[start:end]
            print(inp)
            input_field.send_keys(inp)
            start += step
            end += step
            sleep(0.02)

        for letter in new_text:
            input_field.send_keys(letter)
            sleep(sleeping_time)
        sleep(3)
        soup = BeautifulSoup(driver.page_source,'html.parser')
        place = soup.find('div',{'class':'rank'}).text
        final_wpm = soup.find('div',{'class':'rankPanelWpm'}).text
        print(f'---- Placing: {place}')
        print(f'---- You finished with: {final_wpm}')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    driver = initialize()
    link = input("Give a link if you are with friends: ")
    if link == "":
        start(driver)
    else:
        start(driver,link)
    driver.quit()
