import numpy
import pyautogui
import time
import numpy as np
from PIL import Image


def screen_grab(name=None):
    if name:
        img = pyautogui.screenshot(name, region=(0, 360, 1920, 360))
    else:
        img = pyautogui.screenshot(region=(0, 360, 1920, 360))
    img = img.convert('L')

    img_n = np.asarray(img)
    img_n = (np.round(img_n / 255)).astype(np.uint8)
    if img_n[0, 0] == 0:
        img_n = 1-img_n
    return img_n


def save_img(name):
    img = screen_grab()*255
    im_save = Image.fromarray(img)
    im_save.save(name)


time.sleep(2)
pyautogui.press('space')

cactus_positions = [(0, 0), (0, 0)]
while True:
    screen = screen_grab()
    jumping = screen[330, 60] == 1
    important_strip = list(screen[300, 140:1920])
    if 0 in important_strip:
        closest_cactus = important_strip.index(0)
        if closest_cactus > 160:

            if closest_cactus > cactus_positions[0][0]:
                cactus_positions[0] = (closest_cactus, time.time())
            else:
                cactus_positions[1] = (closest_cactus, time.time())
            if cactus_positions[1][0] > 0:
                speed = (cactus_positions[0][0]-cactus_positions[1][0])/(cactus_positions[1][1]-cactus_positions[0][1])
#                jump_distance = 270+((speed-900)/3)
                seconds_away = closest_cactus/speed
#                if 160 < closest_cactus < jump_distance and not jumping:
                if seconds_away < .31 and not jumping:
                    print("PRESSING")
                    pyautogui.press('space')
                    cactus_positions = [(0, 0), (0, 0)]

'''
                elif jumping and 0 not in screen[300, 0:int(jump_distance)]:
                    print('DOWN')
                    pyautogui.keyDown('down')
                    while screen[330, 60] == 1:
                        screen = screen_grab()
                    pyautogui.keyUp('down')



'''

