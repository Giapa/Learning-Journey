from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import requests

file = open("gr_utf8.txt")
words = file.readlines()
file.close()

driver = webdriver.Firefox()
driver.implicitly_wait(10)

while input("Type yes to enter info: ") != "yes":
    continue

name = input("Your name: ")

driver.find_element_by_id("inputName").send_keys(name)

driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/form/button[1]").click()
sleep(3)

while True:
    try:
        while input("Start round guesses: ") != "yes":
            continue
        soup = BeautifulSoup(driver.page_source,"html.parser")
        word = soup.find("div",{"id":"currentWord"}).text
        word_length = len(word)
        available = []
        letters = []
        for i,letter in enumerate(word):
            if letter != "_":
                letters.append([i,letter])
        check = []

        for i in words:
            if len(letters) > 0:
                if len(i) - 1 == word_length:
                    for y,letter in letters:
                        if letter in i and i.find(letter) == y:
                            check.append(i)
            elif len(i)-1 == word_length:
                check.append(i)
        
        for test in check:
            print(test)
            
    except KeyboardInterrupt:
        pass
