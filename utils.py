import pydirectinput
from time import sleep
import winsound

def press_key(key):
    pydirectinput.press(key)

def hold_key(key, duration = 0.1):
    pydirectinput.keyDown(key)
    sleep(duration)
    pydirectinput.keyUp(key)

def found_alert():
    winsound.Beep(440, 800)

def navigate_menu(current: str, target: str):
    match current:
        case 'main':
            match target:
                case "pokemons":
                    press_key('down')
                    press_key('space')
                case "bag":
                    press_key('right')
                    press_key('space')
                case "exit":
                    press_key('down')
                    press_key('right')
                    press_key('space')