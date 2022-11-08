
"""Bot that can write any message in a loop"""

import time

import pyautogui as pg

print("program will run in 5 sec")
time.sleep(5)
for i in range(10):
    pg.write('You are hacked ')
    time.sleep(0.5)
    pg.press("Enter")
    