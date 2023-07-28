import pyautogui
import time
import pandas

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

pyautogui.click(x=2358, y=365)
pyautogui.write("teste@teste.com")

pyautogui.press("tab")
pyautogui.write("teste")

pyautogui.click(x=2588, y=522 )

tabela = pandas.read_csv("produtos.csv")