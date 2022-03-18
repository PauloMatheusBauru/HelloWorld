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
BB = ["Branco","B","B","B","B"]
BW = ["R", "B", "B", "B", "B", "B"]
BD = ["B","B","B","B","B","B"]
BDB = ["Branco","B","B","B","B","B"]
BDW = ["R","B","B","B","B","B","B"]
BDWB = ["R","B","Branco","B","B","B","B"]
BWB = ["R","Branco","B","B","B","B"]
Bloss = ["B", "B", "B", "B", "B", "B", "B"]
BlossD = ["Branco", "B", "B", "B", "B", "B", "B"]
BlossB = ["B", "B", "Branco", "B", "B", "B", "B"]
BlossB2 = ["Branco", "B", "Branco", "B", "B", "B", "B"]
R = ["R","R","R","R","R"]
RB = ["Branco","R","R","R","R"]
RW = ["B", "R", "R", "R", "R", "R"]
RD = ["R","R","R","R","R","R"]
RDB = ["Branco","R","R","R","R","R"]
RDW = ["B","R","R","R","R","R","R"]
RDWB = ["B","R","Branco","R","R","R","R"]
RWB = ["B","Branco","R","R","R","R"]
RLoss = ["R", "R", "R", "R", "R", "R", "R"]
RLossD = ["Brancp", "R", "R", "R", "R", "R", "R"]
RLossB = ["R", "R", "Branco", "R", "R", "R", "R"]
RLossB2 = ["Branco", "R", "Branco", "R", "R", "R", "R"]
Resultado = []
ResultadoD = []
ResultadoW = []
ResultadoWD = []
ResultadoL = []
Alerta = []

Giros = 0
Win = 0
WinD = 0
Loss = 0
Verificar = 3
Carteira = 65


def Inciar():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    # browser = webdriver.Chrome(chrome_options=options)
    browser = webdriver.Chrome()
    browser.get("https://web.whatsapp.com/")
    ProcurarGrupo = WebDriverWait(browser, 130).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')))
    ProcurarGrupo.send_keys("Teste bot")
    time.sleep(2)
    SelecionarGrupo = WebDriverWait(browser, 130).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div'))).click()
    Varrer()

def Looping():
    print("Looping")



def Resultados():
    global Win
    global WinD
    global Loss
    global Carteira
    global Verificar
    MandarMsg1 = WebDriverWait(browser, 130).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')))
    MandarMsg1.send_keys(f"*Acertamos de primeira: {Win} Vezes*")
    QuebarLinha = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys(Keys.SHIFT + Keys.ENTER)
    MandarMsg1.send_keys(f"*Acertamos dobrando a quantia investida: {WinD} Vezes*")
    QuebarLinha = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys(Keys.SHIFT + Keys.ENTER)
    MandarMsg1.send_keys(f"*Erramos: {Loss} Vezes*")
    QuebarLinha = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys(Keys.SHIFT + Keys.ENTER)
    MandarMsg1.send_keys(f"*O robo tem {Carteira}*")
    EnviarMsg = WebDriverWait(browser, 130).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'))).click()
    Varrer()




def AlertarVermelho():
    MandarMsg1 = WebDriverWait(browser, 130).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')))
    MandarMsg1.send_keys("*Alerta para possivel entrada*")
    QuebarLinha = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys(Keys.SHIFT + Keys.ENTER)
    MandarMsg1.send_keys("Irá Apostar:\r *VERMELHO♦*")
    QuebarLinha = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys(Keys.SHIFT + Keys.ENTER)
    MandarMsg1.send_keys("*Aguarde! ♦*")
    QuebarLinha = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys(Keys.SHIFT + Keys.ENTER)
    MandarMsg1.send_keys("♦Desenvolvido por *B*♦")
    EnviarMsg = WebDriverWait(browser, 130).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'))).click()
    Varrer()

def AlertarPreto():
    MandarMsg = WebDriverWait(browser, 130).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')))
    MandarMsg.send_keys("Alerta para possivel entrada")
    QuebarLinha = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys(Keys.SHIFT + Keys.ENTER)
    MandarMsg.send_keys("Irá Apostar:\r *PRETO ⚫*")
    QuebarLinha = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys(Keys.SHIFT + Keys.ENTER)
    MandarMsg.send_keys("*Aguarde! ⚫*")
    QuebarLinha = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys(Keys.SHIFT + Keys.ENTER)
    MandarMsg.send_keys("⚫Desenvolvido por *B*⚫")
    EnviarMsg = WebDriverWait(browser, 130).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'))).click()
    Varrer()

def ConfirmarVermelho():
    MandarMsg1 = WebDriverWait(browser, 130).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')))
    MandarMsg1.send_keys("*Entrar agora ✅*")
    QuebarLinha = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys(Keys.SHIFT + Keys.ENTER)
    MandarMsg1.send_keys("Apostar:\r *VERMELHO♦*")
    QuebarLinha = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys(Keys.SHIFT + Keys.ENTER)
    MandarMsg1.send_keys("*Entrada Confirmada! ✅*")
    QuebarLinha = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys(Keys.SHIFT + Keys.ENTER)
    MandarMsg1.send_keys("♦Desenvolvido por *B*♦")
    EnviarMsg = WebDriverWait(browser, 130).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'))).click()
    Varrer()

def ConfirmarPreto():
    MandarMsg = WebDriverWait(browser, 130).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')))
    MandarMsg.send_keys("Entrar Agora ✅")
    QuebarLinha = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys(Keys.SHIFT + Keys.ENTER)
    MandarMsg.send_keys("Apostar:\r *PRETO ⚫*")
    QuebarLinha = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys(Keys.SHIFT + Keys.ENTER)
    MandarMsg.send_keys("*Entrada confirmada ✅*")
    QuebarLinha = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys(Keys.SHIFT + Keys.ENTER)
    MandarMsg.send_keys("⚫Desenvolvido por *B*⚫")
    EnviarMsg = WebDriverWait(browser, 130).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'))).click()
    Varrer()

def Varrer():
    time.sleep(2)
    global Win
    global WinD
    global Loss
    global Carteira
    global Verificar
    global Giros
    while True:
        Timer = WebDriverWait(browser, 50).until(EC.presence_of_element_located((By.XPATH,f'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/span'))).text
        if Timer == "0:00":
            time.sleep(23)
            print(Timer)
            try:
                Teste1 = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div/div/div'))).text
            except TimeoutException:
                Teste1 = "Branco"
            try:
                Teste1N = int(Teste1)
                if Teste1N >= 8:
                    Teste1R = re.sub("8|9|10|11|12|13|14", "B", Teste1)
                    Resultado.append(Teste1R)
                    ResultadoL.append(Teste1R)
                    ResultadoW.append(Teste1R)
                    ResultadoD.append(Teste1R)
                    ResultadoWD.append(Teste1R)
                if Teste1N <= 7:
                    Teste1R = re.sub("1|2|3|4|5|6|7", "R", Teste1)
                    Resultado.append(Teste1R)
                    ResultadoL.append(Teste1R)
                    ResultadoW.append(Teste1R)
                    ResultadoD.append(Teste1R)
                    ResultadoWD.append(Teste1R)
            except ValueError:
                Resultado.append("Branco")
                ResultadoW.append("Branco")
                ResultadoL.append("Branco")
                ResultadoD.append("Branco")
                ResultadoWD.append("Branco")
            try:
                Teste2 = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/div'))).text
            except TimeoutException:
                Teste2 = "Branco"
            try:
                Teste2N = int(Teste2)
                if Teste2N >= 8:
                    Teste2R = re.sub("8|9|10|11|12|13|14", "B", Teste2)
                    Resultado.append(Teste2R)
                    ResultadoL.append(Teste2R)
                    ResultadoW.append(Teste2R)
                    ResultadoD.append(Teste2R)
                    ResultadoWD.append(Teste2R)
                if Teste2N <= 7:
                    Teste2R = re.sub("1|2|3|4|5|6|7", "R", Teste2)
                    Resultado.append(Teste2R)
                    ResultadoL.append(Teste2R)
                    ResultadoW.append(Teste2R)
                    ResultadoD.append(Teste2R)
                    ResultadoWD.append(Teste2R)
            except ValueError:
                Resultado.append("Branco")
                ResultadoW.append("Branco")
                ResultadoL.append("Branco")
                ResultadoD.append("Branco")
                ResultadoWD.append("Branco")
            try:
                Teste3 = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div/div'))).text
            except TimeoutException:
                Teste3 = "Branco"
            try:
                Teste3N = int(Teste3)
                if Teste3N >= 8:
                    Teste3R = re.sub("8|9|10|11|12|13|14", "B", Teste3)
                    Resultado.append(Teste3R)
                    ResultadoL.append(Teste3R)
                    ResultadoW.append(Teste3R)
                    ResultadoD.append(Teste3R)
                    ResultadoWD.append(Teste3R)
                if Teste3N <= 7:
                    Teste3R = re.sub("1|2|3|4|5|6|7", "R", Teste3)
                    Resultado.append(Teste3R)
                    ResultadoL.append(Teste3R)
                    ResultadoW.append(Teste3R)
                    ResultadoD.append(Teste3R)
                    ResultadoWD.append(Teste3R)
            except ValueError:
                Resultado.append("Branco")
                ResultadoW.append("Branco")
                ResultadoL.append("Branco")
                ResultadoD.append("Branco")
                ResultadoWD.append("Branco")
            try:
                Teste4 = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[4]/div/div/div'))).text
            except TimeoutException:
                Teste4 = "Branco"
            try:
                Teste4N = int(Teste4)
                if Teste4N >= 8:
                    Teste4R = re.sub("8|9|10|11|12|13|14", "B", Teste4)
                    Resultado.append(Teste4R)
                    ResultadoL.append(Teste4R)
                    ResultadoW.append(Teste4R)
                    ResultadoD.append(Teste4R)
                    ResultadoWD.append(Teste4R)
                if Teste4N <= 7:
                    Teste4R = re.sub("1|2|3|4|5|6|7", "R", Teste4)
                    Resultado.append(Teste4R)
                    ResultadoL.append(Teste4R)
                    ResultadoW.append(Teste4R)
                    ResultadoD.append(Teste4R)
                    ResultadoWD.append(Teste4R)

            except ValueError:
                Resultado.append("Branco")
                ResultadoW.append("Branco")
                ResultadoL.append("Branco")
                ResultadoD.append("Branco")
                ResultadoWD.append("Branco")
            try:
                Teste5 = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[5]/div/div/div'))).text
            except TimeoutException:
                Teste5 = "Branco"
            try:
                Teste5N = int(Teste5)
                if Teste5N >= 8:
                    Teste5R = re.sub("8|9|10|11|12|13|14", "B", Teste5)
                    Resultado.append(Teste5R)
                    ResultadoL.append(Teste5R)
                    ResultadoW.append(Teste5R)
                    ResultadoD.append(Teste5R)
                    ResultadoWD.append(Teste5R)
                if Teste5N <= 7:
                    Teste5R = re.sub("1|2|3|4|5|6|7", "R", Teste5)
                    Resultado.append(Teste5R)
                    ResultadoL.append(Teste5R)
                    ResultadoW.append(Teste5R)
                    ResultadoD.append(Teste5R)
                    ResultadoWD.append(Teste5R)
            except ValueError:
                Resultado.append("Branco")
                ResultadoW.append("Branco")
                ResultadoL.append("Branco")
                ResultadoD.append("Branco")
                ResultadoWD.append("Branco")
            try:
                Teste6 = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[6]/div/div/div'))).text
            except TimeoutException:
                Teste6 = "Branco"
            try:
                Teste6N = int(Teste6)
                if Teste6N >= 8:
                    Teste6R = re.sub("8|9|10|11|12|13|14", "B", Teste6)
                    ResultadoD.append(Teste6R)
                    ResultadoL.append(Teste6R)
                    ResultadoW.append(Teste6R)
                    ResultadoWD.append(Teste6R)
                if Teste6N <= 7:
                    Teste6R = re.sub("1|2|3|4|5|6|7", "R", Teste6)
                    ResultadoD.append(Teste6R)
                    ResultadoL.append(Teste6R)
                    ResultadoW.append(Teste6R)
                    ResultadoWD.append(Teste6R)
            except ValueError:
                Resultado.append("Branco")
                ResultadoW.append("Branco")
                ResultadoL.append("Branco")
                ResultadoD.append("Branco")
                ResultadoWD.append("Branco")
            try:
                Teste7 = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[7]/div/div/div'))).text
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
                ResultadoWD.append("Branco")

                ##### RESULTADOS
            Alerta = Resultado[0:4]
            print("5X TENTAR", Resultado)
            print("6X TENTAR", ResultadoD)
            print("7X ERRAR", ResultadoL)
            print("6X Acertou", ResultadoW)
            print("4x Alerta", Alerta)
            Giros += 1
################ Esperar Errar para começar #####################

            if Verificar == 3:
                Verificar = 0
                while True:
                    time.sleep(1)
                    try:
                        Teste1 = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div/div/div'))).text
                    except TimeoutException:
                        Teste1 = "Branco"
                    try:
                        Teste1N = int(Teste1)
                        if Teste1N >= 8:
                            Teste1R = re.sub("8|9|10|11|12|13|14", "B", Teste1)
                            Resultado.append(Teste1R)
                            ResultadoL.append(Teste1R)
                            ResultadoW.append(Teste1R)
                            ResultadoD.append(Teste1R)
                            ResultadoWD.append(Teste1R)
                        if Teste1N <= 7:
                            Teste1R = re.sub("1|2|3|4|5|6|7", "R", Teste1)
                            Resultado.append(Teste1R)
                            ResultadoL.append(Teste1R)
                            ResultadoW.append(Teste1R)
                            ResultadoD.append(Teste1R)
                            ResultadoWD.append(Teste1R)
                    except ValueError:
                        Resultado.append("Branco")
                        ResultadoW.append("Branco")
                        ResultadoL.append("Branco")
                        ResultadoD.append("Branco")
                        ResultadoWD.append("Branco")
                    try:
                        Teste2 = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.XPATH,
                                                                                                 '/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/div'))).text
                    except TimeoutException:
                        Teste2 = "Branco"
                    try:
                        Teste2N = int(Teste2)
                        if Teste2N >= 8:
                            Teste2R = re.sub("8|9|10|11|12|13|14", "B", Teste2)
                            Resultado.append(Teste2R)
                            ResultadoL.append(Teste2R)
                            ResultadoW.append(Teste2R)
                            ResultadoD.append(Teste2R)
                            ResultadoWD.append(Teste2R)
                        if Teste2N <= 7:
                            Teste2R = re.sub("1|2|3|4|5|6|7", "R", Teste2)
                            Resultado.append(Teste2R)
                            ResultadoL.append(Teste2R)
                            ResultadoW.append(Teste2R)
                            ResultadoD.append(Teste2R)
                            ResultadoWD.append(Teste2R)
                    except ValueError:
                        Resultado.append("Branco")
                        ResultadoW.append("Branco")
                        ResultadoL.append("Branco")
                        ResultadoD.append("Branco")
                        ResultadoWD.append("Branco")
                    try:
                        Teste3 = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.XPATH,
                                                                                                 '/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div/div'))).text
                    except TimeoutException:
                        Teste3 = "Branco"
                    try:
                        Teste3N = int(Teste3)
                        if Teste3N >= 8:
                            Teste3R = re.sub("8|9|10|11|12|13|14", "B", Teste3)
                            Resultado.append(Teste3R)
                            ResultadoL.append(Teste3R)
                            ResultadoW.append(Teste3R)
                            ResultadoD.append(Teste3R)
                            ResultadoWD.append(Teste3R)
                        if Teste3N <= 7:
                            Teste3R = re.sub("1|2|3|4|5|6|7", "R", Teste3)
                            Resultado.append(Teste3R)
                            ResultadoL.append(Teste3R)
                            ResultadoW.append(Teste3R)
                            ResultadoD.append(Teste3R)
                            ResultadoWD.append(Teste3R)
                    except ValueError:
                        Resultado.append("Branco")
                        ResultadoW.append("Branco")
                        ResultadoL.append("Branco")
                        ResultadoD.append("Branco")
                        ResultadoWD.append("Branco")
                    try:
                        Teste4 = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.XPATH,
                                                                                                 '/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[4]/div/div/div'))).text
                    except TimeoutException:
                        Teste4 = "Branco"
                    try:
                        Teste4N = int(Teste4)
                        if Teste4N >= 8:
                            Teste4R = re.sub("8|9|10|11|12|13|14", "B", Teste4)
                            Resultado.append(Teste4R)
                            ResultadoL.append(Teste4R)
                            ResultadoW.append(Teste4R)
                            ResultadoD.append(Teste4R)
                            ResultadoWD.append(Teste4R)
                        if Teste4N <= 7:
                            Teste4R = re.sub("1|2|3|4|5|6|7", "R", Teste4)
                            Resultado.append(Teste4R)
                            ResultadoL.append(Teste4R)
                            ResultadoW.append(Teste4R)
                            ResultadoD.append(Teste4R)
                            ResultadoWD.append(Teste4R)

                    except ValueError:
                        Resultado.append("Branco")
                        ResultadoW.append("Branco")
                        ResultadoL.append("Branco")
                        ResultadoD.append("Branco")
                        ResultadoWD.append("Branco")
                    try:
                        Teste5 = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.XPATH,
                                                                                                 '/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[5]/div/div/div'))).text
                    except TimeoutException:
                        Teste5 = "Branco"
                    try:
                        Teste5N = int(Teste5)
                        if Teste5N >= 8:
                            Teste5R = re.sub("8|9|10|11|12|13|14", "B", Teste5)
                            Resultado.append(Teste5R)
                            ResultadoL.append(Teste5R)
                            ResultadoW.append(Teste5R)
                            ResultadoD.append(Teste5R)
                            ResultadoWD.append(Teste5R)
                        if Teste5N <= 7:
                            Teste5R = re.sub("1|2|3|4|5|6|7", "R", Teste5)
                            Resultado.append(Teste5R)
                            ResultadoL.append(Teste5R)
                            ResultadoW.append(Teste5R)
                            ResultadoD.append(Teste5R)
                            ResultadoWD.append(Teste5R)
                    except ValueError:
                        Resultado.append("Branco")
                        ResultadoW.append("Branco")
                        ResultadoL.append("Branco")
                        ResultadoD.append("Branco")
                        ResultadoWD.append("Branco")
                    try:
                        Teste6 = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.XPATH,
                                                                                                 '/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[6]/div/div/div'))).text
                    except TimeoutException:
                        Teste6 = "Branco"
                    try:
                        Teste6N = int(Teste6)
                        if Teste6N >= 8:
                            Teste6R = re.sub("8|9|10|11|12|13|14", "B", Teste6)
                            ResultadoD.append(Teste6R)
                            ResultadoL.append(Teste6R)
                            ResultadoW.append(Teste6R)
                            ResultadoWD.append(Teste6R)
                        if Teste6N <= 7:
                            Teste6R = re.sub("1|2|3|4|5|6|7", "R", Teste6)
                            ResultadoD.append(Teste6R)
                            ResultadoL.append(Teste6R)
                            ResultadoW.append(Teste6R)
                            ResultadoWD.append(Teste6R)
                    except ValueError:
                        Resultado.append("Branco")
                        ResultadoW.append("Branco")
                        ResultadoL.append("Branco")
                        ResultadoD.append("Branco")
                        ResultadoWD.append("Branco")
                    try:
                        Teste7 = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div[7]/div/div/div'))).text
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
                        ResultadoWD.append("Branco")
                    print("Esperando Uma loss para começar")
                    if ResultadoL == Bloss:
                        print("Errou Dobrado")
                        Varrer()
                    if ResultadoL == RLoss:
                        print("Errou Dobrado")
                        Varrer()
                    if ResultadoL == BlossD:
                        print("Errou Dobrado")
                        Varrer()
                    if ResultadoL == RLossD:
                        print("Errou Dobrado")
                        Varrer()
                    if ResultadoL == BlossB:
                        print("Errou Dobrado")
                        Varrer()
                    if ResultadoL == RLossB:
                        print("Errou Dobrado")
                        Varrer()
                    if ResultadoL == BlossB2:
                        print("Errou Dobrado")
                        Varrer()
                    if ResultadoL == RLossB2:
                        print("Errou Dobrado")
                        Varrer()
                    Alerta = Resultado[0:4]
                    print("5X TENTAR", Resultado)
                    print("6X TENTAR", ResultadoD)
                    print("7X ERRAR", ResultadoL)
                    print("6X Acertou", ResultadoW)
                    print("4x Alerta", Alerta)
                    Resultado.clear()
                    ResultadoD.clear()
                    ResultadoW.clear()
                    ResultadoL.clear()
                    Alerta.clear()


############## FIM DA VERIFICAÇÃO SEGREDO DO SUCESSO ################################
            if ResultadoL == Bloss:
                print("Errou Dobrado")
                Loss += 1
                Carteira -= 10
                time.sleep(80)             ###### Para não repetir função
            if ResultadoL == RLoss:
                print("Errou Dobrado")
                Loss += 1
                Carteira -= 10
                time.sleep(80)             ###### Para não repetir função
            if ResultadoL == BlossD:
                print("Errou Dobrado")
                Loss += 1
                Carteira -= 10
                time.sleep(80)             ###### Para não repetir função
            if ResultadoL == RLossD:
                print("Errou Dobrado")
                Loss += 1
                Carteira -= 10
                time.sleep(80)             ###### Para não repetir função
            if ResultadoL == BlossB:
                print("Errou Dobrado")
                Loss += 1
                Carteira -= 10
                time.sleep(80)             ###### Para não repetir função
            if ResultadoL == RLossB:
                print("Errou Dobrado")
                Loss += 1
                Carteira -= 10
                time.sleep(80)             ###### Para não repetir função
            if ResultadoL == BlossB2:
                print("Errou Dobrado")
                Loss += 1
                Carteira -= 10
                time.sleep(80)             ###### Para não repetir função
            if ResultadoL == RLossB2:
                print("Errou Dobrado")
                Loss += 1
                Carteira -= 10
                time.sleep(80)             ###### Para não repetir função
            elif ResultadoD == RD:
                print("Dobrado")
                # time.sleep(80)             ###### Para não repetir função
            elif ResultadoD == BD:
                print("Dobrado")
                # time.sleep(80)             ###### Para não repetir função
            elif ResultadoD == RDB:
                print("Dobrado")
                # time.sleep(80)             ###### Para não repetir função
            elif ResultadoD == BDB:
                print("Dobrado")
                # time.sleep(80)             ###### Para não repetir função
            elif ResultadoW == BW:
                print("Acerto")
                Carteira += 5
                Win += 1
                Verificar += 1
            elif ResultadoW == RW:
                print("Acerto")
                Carteira += 5
                Win += 1
                Verificar += 1
            elif ResultadoW == BWB:
                print("Acerto Dps do branco")
                Carteira += 5
                Win += 1
                Verificar += 1
            elif ResultadoW == RWB:
                print("Acerto Dps do branco")
                Carteira += 5
                Win += 1
                Verificar += 1
            elif ResultadoWD == BDW:
                print("Acerto")
                Carteira += 5
                Win += 1
                Verificar += 1
            elif ResultadoWD == RDW:
                print("Acerto")
                Carteira += 5
                Win += 1
                Verificar += 1
            elif ResultadoWD == BDWB:
                print("Acerto Dps do branco")
                Carteira += 5
                Win += 1
                Verificar += 1
            elif ResultadoWD == RDWB:
                print("Acerto Dps do branco")
                Carteira += 5
                Win += 1
                Verificar += 1
            elif Resultado == R:
                print("Jogar")
                print("Jogar")
                print("Jogar")
                print("Jogar")
                #ConfirmarPreto()
            elif Resultado == B:
                print("Jogar")
                print("Jogar")
                print("Jogar")
                #ConfirmarPreto()
            elif Alerta == AlertaR:
                print("Alerta")
                print("Alerta")
                #AlertarVermelho()
            elif Alerta == AlertaB:
                print("Alerta")
                print("Alerta")
                #AlertarVermelho()
            elif Resultado == BB:
                print("Jogar Vermelho")
                print("Jogar Vermelho")
                print("Jogar Vermelho")
                #ConfirmarVermelho()
            elif Resultado == RB:
                print("Jogar Preto")
                print("Jogar Preto")
                print("Jogar Preto")
                #ConfirmarPreto()
            elif Giros == 150:
                Resultados()

            print(Win)
            print(Loss)
            print(f"R${Carteira}")
            Resultado.clear()
            ResultadoD.clear()
            ResultadoW.clear()
            ResultadoL.clear()
            Looping()

Inciar()
