from pyfiglet import Figlet
import time
import keyboard as input
import os
import shutil
from changescenes import ChangeScene

f = Figlet(font='ascii___')

currentoption = 0
gamestate = False

print('program started')


def DrawText(text, center=True):
    if(str(text)!= ''):
        if(center is True):
            print(*[x.center(shutil.get_terminal_size().columns) for x in f.renderText(text).split("\n")],sep="\n")
        else:
            print (f.renderText(text))
    else:
        print("[OUR ERROR], please check text {text} <- that should have something, can't be empty")
    pass


def NavigateMenu(key):
    global currentoption
    os.system('cls' if os.name == 'nt' else 'clear')
    if(key == 'up'):
        if currentoption == 0:
            currentoption += 1
        else:
            currentoption = 0
    else:
        if currentoption == 1:
            currentoption -= 1
        else:
            currentoption = 1
        
    DrawMenu()
    pass


def DrawMenu():
    global currentoption

    print('\n\n\n\n\n')

    if(currentoption == 0):
        DrawText('-play-')
        DrawText('exit')
    else:
        DrawText('play')
        DrawText('-exit-')
    pass



def Play():
    global gamestate
    os.system('cls' if os.name == 'nt' else 'clear')
    ChangeScene('GameMain')
    gamestate = True
    pass

def Exit():
    os.system('cls' if os.name == 'nt' else 'clear')
    exit()
    pass



def ClickedButton():
    global currentoption

    if(currentoption == 0):
        Play()
    else:
        Exit()
    pass





while gamestate is False:
    if input.is_pressed('w') or input.is_pressed('up_arrow'):
        NavigateMenu('up')
        time.sleep(1)
    elif input.is_pressed('s') or input.is_pressed('down_arrow'):
        NavigateMenu('down')
        time.sleep(1)
    elif input.is_pressed('esc'):
        break
    elif input.is_pressed('enter'):
        ClickedButton()
        time.sleep(1)



        

