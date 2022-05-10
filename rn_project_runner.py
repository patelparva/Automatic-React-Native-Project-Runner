import os
import time
import pyautogui

path_input=input('Enter the path of the React native project which you want to run. ')
print('Do not touch the keyboard or mouse for few seconds.')

os.system(f"start cmd /k cd {path_input}")

time.sleep(1)
pyautogui.typewrite('expo start')
pyautogui.press('enter')

time.sleep(15)
pyautogui.press('d')

time.sleep(1)
pyautogui.press('a')