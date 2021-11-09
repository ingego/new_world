import  numpy as np
import  cv2 
from PIL import  ImageGrab
from mss import mss
import  time
from datetime import datetime
import pyautogui
from fish import fish

from mouseclicker import smartGetFish

def ml():
    looptime = 60
    now = datetime.now()
    while True:
        screen = ImageGrab.grab(bbox= (0,0,1280,720))
        onPickFishSourceImage = cv2.imread("status_temp/onPickFishTest.png")
        onRedResult = cv2.imread("status_temp/onEnd.png", 0)
        template = np.array(screen)
        searchElement = cv2.cvtColor(onPickFishSourceImage, cv2.COLOR_BGRA2GRAY)
        template = cv2.cvtColor(template, cv2.COLOR_BGRA2GRAY)
        w,h = searchElement.shape[::-1]
        result_search = cv2.matchTemplate(template, searchElement, cv2.TM_CCOEFF_NORMED)       
        res = np.where(result_search > 0.7)
        x = 0
        y = 0
        for pt in zip(*res[::-1]):
            x= int(pt[0])
            y = int(pt[1])
        if(np.mean(res)>0): 
            fish()
            now = datetime.now()
        cv2.rectangle(template,(x, y), (x+w, y+h), 255, 2)

        cv2.imshow("Whatcher",template)
        print((datetime.now() - now).seconds)
        if((datetime.now() - now).seconds >looptime):
            print("loop")
            pyautogui.mouseDown()
            time.sleep(0.3)
            pyautogui.mouseUp()
            now = datetime.now()


        cv2.waitKey(20)
        
