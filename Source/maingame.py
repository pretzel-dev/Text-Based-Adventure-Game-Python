import keyboard as input
import os
import time

CurrentState = 'Main game'


def StartGame():
    print_main_scene()
    pass


def print_main_scene():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('PLAYER')


def print_inventory():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('inventory')
    pass

def change_state(state):
    if(CurrentState == 'Main game'):
        if(state == 'inventory'):
            print_inventory()
    pass




while True:
    if(input.is_pressed('Tab')):
        change_state('inventory')
    if(input.is_pressed('Esc')):
        break