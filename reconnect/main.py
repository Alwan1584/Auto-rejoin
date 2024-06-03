import pyautogui
import time
import pygetwindow as gw
import ctypes
from pygetwindow._pygetwindow_win import getForegroundWindow

image_path = 'E:\\py\\Roblox reconnect\\Images\\reconnect.png'
window = gw.getWindowsWithTitle('Roblox')


def reconnect():
    try:
        location = pyautogui.locateOnScreen(image_path)
        center = pyautogui.center(location)
        pyautogui.click(center, button='Left', click=10)
    except pyautogui.ImageNotFoundException:
        pass

    return print('reconnect attempted')


def r_confirm ():
    #try:
        rbx = gw.getForegroundWindow()
        if rbx != window:
            window.activate()
        else:
            return None
    #except :
        return None

while True:
     r_confirm()
     time.sleep(5)
     reconnect()


# def r_open(lst):
#     r_window = [i for i in lst if i == 'Roblox']
#     return r_window
