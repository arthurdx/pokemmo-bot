import pyautogui
import pydirectinput
import pyscreeze


from utils import *
from time import sleep

#x min = 1092, y min = 388
#x max = 1248, y max = 493

pyautogui.useImageNotFoundException()

def find_trainer() -> bool:
    for trainerimg in ("face", "back"):
            try:
                print(f"Looking for trainer {trainerimg}")
                local = pyautogui.locateOnScreen('images/trainer' + trainerimg + '.png', confidence=0.8)
                if trainerimg == "face":
                    hold_key('up', 0.6)
                    print(f"Trainer face found at: {local}")
                elif trainerimg == "back":
                    hold_key('down', 0.6)
                    print(f"Trainer back found at: {local}")
                    return True
            except pyautogui.ImageNotFoundException:
                print("Trainer not found")
    return False
            
def in_battle() -> bool:
    try:
        locations = list(pyautogui.locateAllOnScreen('images/hp_bar.png', confidence=0.8))
        bar_nums = round(len(locations)/12)
        if bar_nums > 0:
            print("In battle")
            print(bar_nums)
            if bar_nums > 1:
                print("Double battle")
            return True
    except pyscreeze.ImageNotFoundException:
        print("Not in battle, resuming search")
    return False
    
def is_charmander() -> bool:
    try:
        pyautogui.locateOnScreen('images/charmander_name.png', confidence=0.8, grayscale=True)
        return True
    except pyautogui.ImageNotFoundException:
        return False

def is_ekans() -> bool:
    try:
        pyautogui.locateOnScreen('images/ekans_name.png', confidence=0.8, grayscale=True)
        return True
    except pyautogui.ImageNotFoundException:
        return False

def is_shiny() -> bool:
    try:
        pyautogui.locateOnScreen('images/shiny.png', confidence=0.8)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    
def catch_pokemon():
    pydirectinput.press('space')
    sleep(10)
    pydirectinput.press('space')
    sleep(0.2)
    pydirectinput.press('right')
    sleep(0.2)
    pydirectinput.press('space')
    sleep(8)
    pydirectinput.press('right')
    sleep(0.2)
    pydirectinput.press('space')
    sleep(0.2)
    navigate_menu()

def flee():
    navigate_menu('main', 'exit')
    sleep(4)
    

# def navigate_menu():
#     for img in ("battle_itens", "pokeballs", "medicine", "berries"):
#         try:
#             print(f"Looking for {img}")
#             local = pyautogui.locateOnScreen('images/' + img + '.png', confidence=0.8)
#             print(f"{img} found at: {local}")
#             if img == "pokeballs" and local:
#                 pydirectinput.press('space')
#             if img == "battle_itens":
#                 pydirectinput.press('left')
#             if img == "medicine":
#                 pydirectinput.press(['right', 'right'])
#             if img == "berries":
#                 pydirectinput.press('right')
#         except pyautogui.ImageNotFoundException:
#             print(f"{img} not found")

def lure_ended() -> bool:
    try:
        pyautogui.locateOnScreen('images/lure_ended.png', confidence=0.8)
        pydirectinput.press('z')
        return True
    except pyautogui.ImageNotFoundException:
        return False

def search_encounter():
    pass
    
if __name__ == "__main__":
    sleep(2)
    try:
        while True:
            if lure_ended():
                    print("Lure ended, reusing")
            if find_trainer():
                continue
            else:
                if in_battle():
                    if is_shiny():
                        print("Shiny found")
                        found_alert()
                        # catch_pokemon()
                    elif is_charmander():
                        print("Charmander found")
                        found_alert()
                        # catch_pokemon()
                    
                    elif is_ekans():
                        print("Ekans found, waiting intimidade animation to flee")
                        sleep(12)
                        flee()
                    else:
                        print("Not a Charmander, fleeing")
                        sleep(6)
                        flee()

    except KeyboardInterrupt:
        pass
        
    
