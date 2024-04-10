"""
This module contains functions for generating random mouse movements using the pyautogui library.
"""
import random
import time
import pyautogui as pag

def random_mouse_movement():
    """
    This function generates random mouse movements within a specified range.
    The X position of the mouse is randomly chosen between 500 and 700,
    and the Y position of the mouse is randomly chosen between 100 and 800.
    The function uses the pyautogui library to move the mouse cursor.
    """
    while True:
        x = random.randint(500, 700) # X position of the mouse from 500 to 700
        y = random.randint(100, 800) # Y position of the mouse from 100 to 800
        pag.moveTo(x, y, 0.5) # Moves the mouse to (x,y) for 0.5 seconds 
        time.sleep(15) # Sleeps for 15 seconds before making another movement

if __name__ == "__main__":
    random_mouse_movement()
