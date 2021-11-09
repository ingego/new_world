import time
import pyautogui
from PIL import  ImageGrab
from mss import mss
import  numpy as np
import  cv2 
from datetime import datetime

screenDuration = 20  # update screen ( grap and open_cv)
fishTime = 22 # seconds fish 

def smartGetFish():
    startTime = datetime.now()

    while True:  
        screen = ImageGrab.grab(bbox= (0,0,1280,720))
        onRedResult = cv2.imread("status_temp/searchFish.jpg")
        template = np.array(screen)
        template = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)
        low_range = np.array([16, 14, 56])
        upper_range = np.array([21, 17, 132])

        mask = cv2.inRange(template, low_range, upper_range)
        cv2.waitKey(screenDuration)
        duration = datetime.now() - startTime
        if(np.mean(mask)==0.0):
            pyautogui.mouseDown()

            if(duration.seconds > fishTime):
                break
                
        if ( np.mean(mask) > 0.0):
             pyautogui.mouseUp()