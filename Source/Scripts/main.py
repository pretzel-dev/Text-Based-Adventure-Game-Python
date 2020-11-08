# Menu script

from pyfiglet import Figlet
import time
import keyboard as input

f = Figlet(font='ascii___')

def DrawText(text):
    if(str(text)!=""):
        return(f.renderText(text))
    else:
        return("[OUR ERROR], please check size {size} <- that shouldn't be 0 and text {text} <- that should have something, can't be empty")



def DrawMenu():
    return(DrawText("play") + "\n" + DrawText("exit"))



print(DrawMenu())
    
