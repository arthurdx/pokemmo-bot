import pyautogui
import pyscreeze

# Definindo algumas localizações de exemplo
locations = [
    pyscreeze.Box(100, 100, 50, 50),
    pyscreeze.Box(400, 300, 50, 50),
    pyscreeze.Box(700, 500, 50, 50)
]

# Definindo o centro da tela (por exemplo, para uma tela de 1920x1080)
screen_center = (960, 540)

# Encontrando a localização mais próxima do centro
location = min(locations, key=lambda loc: ((loc.left + loc.width / 2 - screen_center[0]) ** 2 + (loc.top + loc.height / 2 - screen_center[1]) ** 2) ** 0.5)

pyautogui.dragTo(pyautogui.center(location))
