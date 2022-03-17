from win10toast import ToastNotifier
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import re


options = webdriver.ChromeOptions()
options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options=options)
browser.get("https://blaze.com/pt/games/double")
AlertaB = ["B","B","B","B"]
AlertaR = ["R","R","R","R"]
B = ["B","B","B","B","B"]
BW = ["R","B","B","B","B","B"]
BD = ["B","B","B","B","B","B"]
BDW = ["R","B","B","B","B","B","B"]
Bloss = ["B","B","B","B","B","B","B"]
R = ["R","R","R","R","R"]
RW = ["B","R","R","R","R","R"]
RD = ["R","R","R","R","R","R"]
RDW = ["B","R","R","R","R","R","R"]
RLoss = ["R","R","R","R","R","R","R"]
Resultado = []
ResultadoD = []
ResultadoW = []
ResultadoWD = []
ResultadoL = []
Alerta = []

Win = 0
WinD = 0
Loss = 0


def MSGWHATS():
    print("Whatszapp")
    Varrer()

def Varrer():
    time.sleep(2)
    global Win
    global WinD
    global Loss
    while True:
        Timer = WebDriverWait(browser, 50).until(EC.presence_of_element_located((By.XPATH,f'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/span'))).text
        print(Timer)
        if Timer == "0:00":
            time.sleep(18)
            try:
                Teste1 = WebDriverWait(browser, 50).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div/div/div'))).text
            except TimeoutException:
                Teste1 = "Branco"
            try:
                Teste1N = int(Teste1)
                if Teste1N >= 8:
                    Teste1R = re.sub("8|9|10|11|12|13|14", "B", Teste1)
                    Resultado.append(Teste1R)
                if Teste1N <= 7:
                    Teste1R = re.sub("1|2|3|4|5|6|7", "R", Teste1)
                    Resultado.append(Teste1R)
            except ValueError:
                Resultado.append("Branco")
            try:
                Teste2 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/div'))).text
            except TimeoutException:
                Teste2 = "Branco"
            try:
                Teste2N = int(Teste2)
                if Teste2N >= 8:
                    Teste2R = re.sub("8|9|10|11|12|13|14", "B", Teste2)
                    Resultado.append(Teste2R)
                if Teste2N <= 7:
                    Teste2R = re.sub("1|2|3|4|5|6|7", "R", Teste2)
                    Resultado.append(Teste2R)
            except ValueError:
                Resultado.append("Branco")
            try:
                Teste3 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div/div'))).text
            except TimeoutException:
                Teste3 = "Branco"
            try:
                Teste3N = int(Teste3)
                if Teste3N >= 8:
                    Teste3R = re.sub("8|9|10|11|12|13|14", "B", Teste3)
                    Resultado.append(Teste3R)
                if Teste3N <= 7:
                    Teste3R = re.sub("1|2|3|4|5|6|7", "R", Teste3)
                    Resultado.append(Teste3R)
            except ValueError:
                Resultado.append("Branco")
            try:
                Teste4 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[4]/div/div/div'))).text
            except TimeoutException:
                Teste4 = "Branco"
            try:
                Teste4N = int(Teste4)
                if Teste4N >= 8:
                    Teste4R = re.sub("8|9|10|11|12|13|14", "B", Teste4)
                    Resultado.append(Teste4R)
                if Teste4N <= 7:
                    Teste4R = re.sub("1|2|3|4|5|6|7", "R", Teste4)
                    Resultado.append(Teste4R)
            except ValueError:
                Resultado.append("Branco")
            try:
                Teste5 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[5]/div/div/div'))).text
            except TimeoutException:
                Teste5 = "Branco"
            try:
                Teste5N = int(Teste5)
                if Teste5N >= 8:
                    Teste5R = re.sub("8|9|10|11|12|13|14", "B", Teste5)
                    Resultado.append(Teste5R)
                if Teste5N <= 7:
                    Teste5R = re.sub("1|2|3|4|5|6|7", "R", Teste5)
                    Resultado.append(Teste5R)
            except ValueError:
                Resultado.append("Branco")
            try:
                Teste6 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[6]/div/div/div'))).text
            except TimeoutException:
                Teste6 = "Branco"
            try:
                Teste6N = int(Teste6)
                ConvertResultado = str(Resultado)[2:-2]
                ResultadoD.append(ConvertResultado)
                ResultadoL.append(ConvertResultado)
                ResultadoW.append(ConvertResultado)
                if Teste6N >= 8:
                    Teste6R = re.sub("8|9|10|11|12|13|14", "B", Teste6)
                    ResultadoD.append(Teste6R)
                    ResultadoL.append(Teste6R)
                if Teste6N <= 7:
                    Teste6R = re.sub("1|2|3|4|5|6|7", "R", Teste6)
                    ResultadoD.append(Teste6R)
                    ResultadoL.append(Teste6R)
            except ValueError:
                Resultado.append("Branco")
            try:
                Teste7 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[7]/div/div/div'))).text
            except TimeoutException:
                Teste7 = "Branco"
            try:
                Teste7N = int(Teste7)
                if Teste7N >= 8:
                    Teste7R = re.sub("8|9|10|11|12|13|14", "B", Teste7)
                    ResultadoL.append(Teste7R)
                    ResultadoWD.append(Teste7R)
                if Teste7N <= 7:
                    Teste7R = re.sub("1|2|3|4|5|6|7", "R", Teste7)
                    ResultadoL.append(Teste7R)
                    ResultadoWD.append(Teste7R)
            except ValueError:
                ResultadoL.append("Branco")
                ResultadoW.append("Branco")

                ##### RESULTADOS
            Alerta = Resultado[0:4]
            print("5X TENTAR", Resultado)
            print("6X TENTAR", ResultadoD)
            print("7X ERRAR", ResultadoL)
            print("7X Acertou", ResultadoW)
            print("4x Alerta", Alerta)
            if Alerta == AlertaR:
                print("Alertar")
            if Alerta == AlertaB:
                print("Alertar")
            if Resultado == R:
                toaster = ToastNotifier()
                toaster.show_toast("Jogue no Preto", "Caso perca dobre na mesma cor! 1X",icon_path=r"C:\Users\User\Desktop\ProgramaAutoedit\IconesPrograma\Icone.ico", threaded=True)
            if Resultado == B:
                toaster = ToastNotifier()
                toaster.show_toast("Jogue no Vermelho", "Caso perca dobre na mesma cor! 1X",icon_path=r"C:\Users\User\Desktop\ProgramaAutoedit\IconesPrograma\Icone.ico",threaded=True)
            if ResultadoL == Bloss:
                Loss += 1
                print("Errou")
                #time.sleep(100)             ###### Para não repetir função
            if ResultadoL == RLoss:
                Loss += 1
                print("Errou")
                #time.sleep(100)             ###### Para não repetir função
            if ResultadoD == RD:
                print("Dobrado")
                # time.sleep(40)             ###### Para não repetir função
            if ResultadoD == BD:
                print("Dobrado")
                # time.sleep(40)             ###### Para não repetir função
            if ResultadoW == BW:
                print("Acerto")
                Win += 1
            if ResultadoW == RW:
                print("Acerto")
                Win += 1
            if ResultadoWD == BDW:
                WinD += 1
                print("AcertoDobrado")
            if ResultadoWD == RDW:
                WindD += 1
                print("AcertoDobrado")
            Resultado.clear()
            ResultadoD.clear()
            ResultadoW.clear()
            ResultadoL.clear()
            print(Win)
            print(WinD)
            print(Loss)
            MSGWHATS()

Varrer()
