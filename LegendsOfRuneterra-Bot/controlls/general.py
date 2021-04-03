#Screen class for controlling resolutions
class Screen():
    
    #Init gui 
    def __init__(self,gui):
        self.gui = gui
    
    #Return screen res
    def get_size(self):
        size = self.gui.size()
        width = size.width
        height = size.height
        return width,height

    #Check if window is active
    def check_home(self):
        active = self.gui.getActiveWindow()
        if active is not None :
            if active.title == "Legends of Runeterra":
                return True
        return False