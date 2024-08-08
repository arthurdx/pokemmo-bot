import pydirectinput
from time import sleep
import winsound
import pyautogui

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
                case "fight":
                    press_key('space')
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
                case _:
                    print("Invalid target")
        case 'fight':
            match target:
                case "false_swipe":
                    press_key('space')
                case "spore":
                    press_key('right')
                    press_key('space')
                case "soak":
                    press_key('right')
                    press_key('down')
                    press_key('space')
                case _:
                    print("Invalid target")
        case 'bag':
            match target:
                case "pokeball":
                    press_key('space')
                case _:
                    print("Invalid target")
        case _:
            print("Invalid current")

#substitute all is_"something" functions with a single function that receives the image name

def image_found(image_name: str) -> bool:
    try:
        pyautogui.locateOnScreen(f'images/{image_name}.png', confidence=0.8, grayscale=True)
        return True
    except pyautogui.ImageNotFoundException:
        return False