#please share it like that or improve it as you can
#
#by someone

import os
import sys
import time
import webbrowser
import pyautogui


nTab = input("How many tab ?(max 9): ")
nExec = input("How many refresh : ")

def open_close(url="https://www.rt.com/"):
    webbrowser.open(url)
    print("Page open")
    time.sleep(2)




def tab_refresh(y):
    pyautogui.hotkey('ctrl', str(y))
    pyautogui.hotkey('ctrl', 'F5')

for i in range(0, int(nTab), 1):

    open_close()

cible = 1

for i in range(0, int(nExec), 1):

    tab_refresh(cible)
    time.sleep(2)
    if cible == int(nTab):
        cible = 0
    cible += 1
