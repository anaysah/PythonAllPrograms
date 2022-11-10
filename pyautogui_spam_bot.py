import pyautogui as pg
import time
time.sleep(10)
text=["hero","king","nothing","help"]
a="Kunal is a "
for i in text:
    pg.write(a+""+i)
    pg.press("enter")
