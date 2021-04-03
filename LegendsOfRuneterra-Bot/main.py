import pyautogui
from controlls.general import Screen
from controlls.mouse import Mouse
from controlls.keyboard import Keyboard
import sys
import time

#Get size of screen and check it is the correct resolution
def valid_size(screen):
    width,height = screen.get_size()
    if  width != '1920' and height != '1080' :
        print('Valid resolution')
        return True
    else:
        print("Invalid resolution")
        return False

if __name__ == "__main__":
    #Init components
    gui = pyautogui
    screen = Screen(gui)
    mouse = Mouse(gui)
    keyboard = Keyboard(gui)

    #Check resolution
    valid = valid_size(screen)
    #Exit is res is not valid
    if valid is False:
        sys.exit()

    #Click to search
    mouse.goto_search()
    time.sleep(1)
    #Type LoR
    keyboard.type_lor()
    print("Opening LoR")

    #Wait until LoR becames active
    while not screen.check_home():
        continue

    #Wait for game to load everything
    time.sleep(30)
    print("Opened LoR")

    #Click to Play -> Vs AI
    mouse.goto_bots()
    print("Start bot surrender")

    #Choose a random deck between the first 4
    mouse.choose_deck()

    #Surrender for 10 times
    for i in range(10):
        mouse.surrender_bots()
        print(f"Surrendered {i+1} times")

    print("Finished surrendering with bots")