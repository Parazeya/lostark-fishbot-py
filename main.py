import numpy
import pyautogui
from cv2 import cv2
import time
from time import gmtime, strftime
import random
import datetime
from datetime import datetime
import time

class screen:
    weight = 1920
    height = 1080


flag = "pulled"
lure = False

template = cv2.imread("template.png", 0)
poplavok = cv2.imread("poplavok.png", 0)

print(strftime("%H:%M:%S", gmtime()), "[Старт]")
time.sleep(5)

if(lure == True):
    LureTime = int(time.time()) + 90
    print(strftime("%H:%M:%S", gmtime()), "[Бросаю прикормку]")
    pyautogui.keyDown('d')
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyUp('d')
    time.sleep(random.uniform(3.5, 4.0))


while(1):
    if flag == "pulled":
        print(strftime("%H:%M:%S", gmtime()), "[Начинаю рыбачить]")
        pyautogui.keyDown('w')
        time.sleep(random.uniform(0.05, 0.1))
        pyautogui.keyUp('w')
        flag = "thrown"
        time.sleep(random.uniform(4.5, 5.5))

    image = pyautogui.screenshot(
        region=(screen.weight/2 - 100, screen.height/2 - 150, 200, 200))
    image = cv2.cvtColor(numpy.array(image), 0)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    template_coordinates = cv2.matchTemplate(
        image, template, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where(template_coordinates >= 0.85)

    if len(loc[0]) > 0:
        if flag == "thrown":
            print(strftime("%H:%M:%S", gmtime()), "[Яяяяяяяяяяяяяяязь]")
            time.sleep(random.uniform(0.2, 1.0))
            pyautogui.keyDown('w')
            time.sleep(random.uniform(0.05, 0.1))
            pyautogui.keyUp('w')
            flag = "pulled"
            time.sleep(random.uniform(9.5, 10.5))

    poplavok_coordinates = cv2.matchTemplate(
        image, poplavok, cv2.TM_CCOEFF_NORMED)
    poplavok_loc = numpy.where(poplavok_coordinates >= 1.0)

    if len(poplavok_loc[0]) == 0 and flag == "pulled":
        if lure == True and int(time.time()) >= LureTime:
            print(strftime("%H:%M:%S", gmtime()), "[Бросаю прикормку]")
            pyautogui.keyDown('d')
            time.sleep(random.uniform(0.05, 0.1))
            pyautogui.keyUp('d')
            time.sleep(random.uniform(5.5, 6.5))

        print(strftime("%H:%M:%S", gmtime()), "[Начинаю рыбачить]")
        pyautogui.keyDown('w')
        time.sleep(random.uniform(0.05, 0.1))
        pyautogui.keyUp('w')
        flag = "thrown"
        time.sleep(random.uniform(4.5, 6.5))

    print(strftime("%H:%M:%S", gmtime()), "Not time yet!")