import time

#Keyboard class for controlling keyboard movement
class Keyboard():
    
    #Init keyboard
    def __init__(self,gui):
        self.keyboard = gui
    
    #Type LoR in search
    def type_lor(self):
        self.keyboard.write("Legends of Runeterra")
        time.sleep(1)
        self.keyboard.press("enter")