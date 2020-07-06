import pyautogui
import time


file = open('LyricsHere.txt','r')

print("Starts in 5 seconds.")
time.sleep(5)


for line in file:
    for word in line.split():
        pyautogui.write(word)
        pyautogui.press('enter')
