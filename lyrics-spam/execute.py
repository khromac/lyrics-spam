import pyautogui
import time


file = open('LyricsHere.txt','r')

print("Starts in 5 seconds.")
time.sleep(5)


for line in file:
    for word in line.split():
        if (pyautogui.press('ctrl')):
            break
        else:
            pyautogui.write(word)
            pyautogui.press('enter')
