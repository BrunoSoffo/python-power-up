import pyautogui
import time

# pyautogui.write -> escreve um texto
# pyautogui.press -> aperta uma tecla
# pyautogui.click -> clica em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas


pyautogui.PAUSE = 0.3
# define o tempo de espera para cada comando pyautogui

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

