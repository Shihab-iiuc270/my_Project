import pyautogui
from time import sleep
sleep(5)
for i in range(2):
    pyautogui.write('hi',interval=0.25)
    pyautogui.press('enter')