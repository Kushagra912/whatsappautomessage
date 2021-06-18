import pyautogui
import time
f=5
while f>0:
    time.sleep(3)
    pyautogui.typewrite("bhai palwal se ho ?")
    time.sleep(2)
    pyautogui.press("enter")
    f=f-1
