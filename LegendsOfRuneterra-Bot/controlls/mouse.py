import random
import time

#Mouse class for controlling mouse movement
class Mouse():
    
    #Init mouse
    def __init__(self,gui):
        self.mouse = gui
    
    #Click at search
    def goto_search(self):
        self.mouse.click(176,1064)
    
    #Go to vs Ai category
    def goto_bots(self):
        self.mouse.click(79,371)
        time.sleep(random.uniform(1,2.3))
        self.mouse.click(301,344)
        time.sleep(random.uniform(1,2.6))

    #Choose a random deck
    def choose_deck(self):
        decks = [(666,317),(1005,246),(1316,264),(1661,267)]
        deck_number = random.randint(0,3)
        choosen_deck = decks[deck_number]
        width = choosen_deck[0]
        height = choosen_deck[1]
        self.mouse.click(width,height)
        time.sleep(random.uniform(1,2.2))
        
    #Complete the whole surrender proccess
    def surrender_bots(self):
        self.mouse.click(1593,967)
        time.sleep(random.uniform(1,2.4))
        time.sleep(20)
        self.mouse.click(1841,55)
        time.sleep(random.uniform(2,3.2))
        self.mouse.click(806,891)
        time.sleep(random.uniform(2,3.2))
        self.mouse.click(1092,605)
        time.sleep(random.uniform(10,13))
        self.mouse.click(1288,985)
        time.sleep(random.uniform(2,3.2))
        
