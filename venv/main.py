import time
import webbrowser as wb

import pyautogui

wb.open("web.whatsapp.com")
time.sleep(40)
# 100 times the message will be sent
for i in range(16):
    pyautogui.press("G")
    pyautogui.press("o")
    pyautogui.press("o")
    pyautogui.press("d")
    pyautogui.press("")
    pyautogui.press(" ")
    pyautogui.press("M")
    pyautogui.press("o")
    pyautogui.press("r")
    pyautogui.press("n")
    pyautogui.press("i")
    pyautogui.press("n")
    pyautogui.press("g")

    pyautogui.press("enter")
