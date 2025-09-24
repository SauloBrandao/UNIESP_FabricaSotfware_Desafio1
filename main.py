import time
import pyautogui 
import pandas 

pyautogui.PAUSE = 0.5

navegador = input("Digite seu navegador: ")
pagina = input("Digite a pagina de cadastro: ")

pyautogui.press("win")
pyautogui.write(navegador)
pyautogui.press("enter")

pyautogui.write(pagina)
pyautogui.press("enter")

time.sleep(2)


tabela = pandas.read_csv("desafio_rpa.xlsx - Planilha1.csv")

for linha in tabela.index:

    pyautogui.click(x=1035, y=441)
    nome = tabela.loc[linha, "Nome"]
    pyautogui.write(nome)

    pyautogui.click(x=1034, y=517)
    sobrenome = tabela.loc[linha, "Sobrenome"]
    pyautogui.write(sobrenome)
    
    pyautogui.press("tab")
    email = tabela.loc[linha, "Email"]
    pyautogui.write(email)

    pyautogui.press("tab")
    empresa = tabela.loc[linha, "Empresa"]
    pyautogui.write(empresa)

    pyautogui.click(x=631, y=767)

    time.sleep(3)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(3)

print("automação finalizada ;)")