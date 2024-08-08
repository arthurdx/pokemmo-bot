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
            
def in_battle() -> int:
    try:
        locations = list(pyautogui.locateAllOnScreen('images/hp_bar.png', confidence=0.8))
        bar_nums = round(len(locations)/12)
        if bar_nums > 0:
            print("In battle")
            print(bar_nums)
            if bar_nums > 1:
                print("Double battle")
                return 2
            return 1
    except pyscreeze.ImageNotFoundException:
        print("Not in battle, resuming search")
    return 0
    
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
    
def is_male() -> bool:
    for maleimg in ('day', 'night'):
        try:
            pyautogui.locateOnScreen('images/male_' + maleimg + '.png', confidence=0.8)
            return True
        except pyautogui.ImageNotFoundException:
            pass
    return False
    
def caught_pokemon() -> bool:
    try:
        pyautogui.locateOnScreen('images/caught.png', confidence=0.8)
        return True
    except pyautogui.ImageNotFoundException:
        return False

def catch_pokemon():
    sleep(8)
    navigate_menu('main', 'fight')
    navigate_menu('fight', 'false_swipe')
    sleep(11)
    throw_pokeball()

def throw_pokeball():
    navigate_menu('main', 'bag')
    navigate_menu('bag', 'pokeball')

def flee():
    navigate_menu('main', 'exit')
    sleep(4)

def catch_charmander():
    sleep(8)
    navigate_menu('main', 'fight')
    navigate_menu('fight', 'false_swipe')
    sleep(12)
    navigate_menu('main', 'fight')
    navigate_menu('fight', 'spore')
    sleep(15)
    throw_pokeball()

def throw_pokeball():
    navigate_menu('main', 'bag')
    navigate_menu('bag', 'pokeball')

def flee():
    navigate_menu('main', 'exit')
    sleep(2)

def check_ivs():
    try:
        location = pyautogui.locateOnScreen('images/ivs.png', confidence=0.8)
        pyautogui.moveTo(pyautogui.center(location))
        pyautogui.click()
    except pyautogui.ImageNotFoundException:
        print("IVs not found")
    
def has_31_iv():
    try:
        pyautogui.locateOnScreen('images/31_iv.png', confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    
#pc 1 = 725, 417
#pc 2 = 913, 417
def release():
    screen_width, screen_height = pyautogui.size()
    screen_center = (screen_width / 2, screen_height / 2)
    try:
        locations = list(pyautogui.locateAllOnScreen('images/pc.png', confidence=0.8))
        pcs_number = round(len(locations)/2)
        print(f"PCs found: {pcs_number}")
        if pcs_number == 1:
            location = min(locations, key=lambda loc: ((loc.left + loc.width / 2 - screen_center[0]) ** 2 + (loc.top + loc.height / 2 - screen_center[1]) ** 2) ** 0.5)
            pyautogui.moveTo(pyautogui.center(location))
            pyautogui.click()
            
    except pyscreeze.ImageNotFoundException:
        print("PC not found")
    try:
        location = pyautogui.locateOnScreen('images/release.png', confidence=0.8)
        pyautogui.moveTo(pyautogui.center(location))
        pyautogui.click()
        sleep(0.8)
        pydirectinput.press('up')
        pydirectinput.press('z')
    except pyautogui.ImageNotFoundException:
        print("Release not found")
    
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

def is_asleep() -> bool:
    try:
        pyautogui.locateOnScreen('images/asleep_status.png', confidence=0.8)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    
def use_spore():
    navigate_menu('main', 'fight')
    navigate_menu('fight', 'spore')
    sleep(15)
    
if __name__ == "__main__":
    sleep(2)
    try:
        while True:
            if lure_ended():
                    print("Lure ended, reusing")
            if find_trainer():
                continue
            else:
                num_enemies = in_battle()
                if num_enemies > 0:
                    if is_shiny():
                        print("Shiny found")
                        found_alert()
                        catch_pokemon()
                    elif is_charmander():
                        print("Charmander found, catch")
                        catch_charmander()
                        sleep(14)
                        while not caught_pokemon():
                            throw_pokeball()
                            sleep(14)
                            if not is_asleep():
                                use_spore()

                        pydirectinput.press('esc')
                    elif is_male() and num_enemies < 2:
                        print("found male breeder, catch")
                        if is_ekans():
                            sleep(8)
                        catch_pokemon()
                        sleep(14)
                        while not caught_pokemon():
                            throw_pokeball()
                            sleep(14)
                        check_ivs()
                        sleep(2)
                        if has_31_iv():
                            print("Keeping")
                            sleep(2)
                            pydirectinput.press('esc')
                        else:
                            print("Releasing")
                            sleep(2)
                            release()
                            
                    else:
                        if is_ekans():
                            sleep(8)
                        print("undesired pokemon, fleeing")
                        sleep(6)
                        flee()

    except KeyboardInterrupt:
        pass
        
    
