import  numpy as np
import  cv2 
from PIL import  ImageGrab
from mss import mss
import  time
from datetime import datetime
import pyautogui

#test
#print(":")
from mouseclicker import smartGetFish
def fish(): 
    smartGetFish()
    pyautogui.click()
    time.sleep(5)
    print("next loop fish")

    time.sleep(1)
    pyautogui.mouseDown()
    
    time.sleep(0.3)
    pyautogui.mouseUp()
