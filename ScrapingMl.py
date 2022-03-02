from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

x = 0
y = 1
browser = webdriver.Chrome()
url = input('Url: ')
browser.maximize_window()
browser.get(url)
NomeVendedor = browser.find_element_by_class_name("store-info__name").text
AceitarCookie = WebDriverWait(browser, 40).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/button'))).click()
VerTodosAnuncios = WebDriverWait(browser, 40).until(EC.presence_of_element_located((By.XPATH, f'/html/body/main/div/div/div[2]/div[2]/div[2]/span/a'))).click()
while True:
    if x == 3:
        y += 1
        x = 1
    else:
        x += 1
    ClicarAnuncio = WebDriverWait(browser, 40).until(EC.presence_of_element_located((By.XPATH, f'/html/body/main/div/div/section/ol[{y}]/li[{x}]/div/div'))).click()
    Titulo = WebDriverWait(browser, 40).until(EC.presence_of_element_located((By.CLASS_NAME, 'ui-pdp-title'))).text
    Preco = WebDriverWait(browser, 40).until(EC.presence_of_element_located((By.CLASS_NAME, 'andes-money-amount__fraction'))).text
    Descricao = WebDriverWait(browser, 40).until(EC.presence_of_element_located((By.CLASS_NAME, 'ui-pdp-description__content'))).text
    browser.back()
    print (Preco)
    Preco = int(Preco)

    # # # # CALCULAR O PREÇO # # # # #

    if Preco < 50:
        Preco =+ 15
        print(Preco)
    elif Preco > 50:
        Preco += 30
        print(Preco)


    print(Titulo)
    print(Preco)
    print(Descricao)
