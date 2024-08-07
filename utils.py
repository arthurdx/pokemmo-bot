import pydirectinput
from time import sleep
import winsound

def hold_key(key, duration = 0.1):
    pydirectinput.keyDown(key)
    sleep(duration)
    pydirectinput.keyUp(key)

def found_alert():
    winsound.Beep(440, 800)