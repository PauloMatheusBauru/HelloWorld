from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

x = 0
y = 1
sku = 0
browser = webdriver.Chrome()
url = input('Url: ')
browser.maximize_window()
browser.get(url)
VendedorName = browser.find_element_by_class_name("store-info__name").text
AcceptCokies = WebDriverWait(browser, 40).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[2]/div/button'))).click()
VerTodosAnuncios = WebDriverWait(browser, 40).until(EC.presence_of_element_located((By.CLASS_NAME,'publications__subtitle'))).click()
os.mkdir(fr'C:\Users\User\Desktop\TESTE\{VendedorName}')
while True:
    if x == 3:
        y += 1
        x = 1
        sku += 1
    else:
        x += 1
        sku += 1
    try:
        ClickAnnounce = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, f'/html/body/main/div/div/section/ol[{y}]/li[{x}]/div/div'))).click()
        Title = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'ui-pdp-title'))).text
        Price = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'andes-money-amount__fraction'))).text
        Description = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'ui-pdp-description__content'))).text
        element = browser.find_element_by_class_name('ui-pdp-gallery__figure')
        element.location_once_scrolled_into_view
        with open(fr'C:\Users\User\Desktop\TESTE\{VendedorName}\{sku}.png', 'wb') as file:
            file.write(browser.find_element_by_class_name('ui-pdp-gallery__figure').screenshot_as_png)
        browser.back()
        arquivo = open(fr"C:\Users\User\Desktop\TESTE\{VendedorName}\Titulo{sku}.txt", "a")
        arquivo.write(f"{Title}")
        arquivo1 = open(fr"C:\Users\User\Desktop\TESTE\{VendedorName}\Preco{sku}.txt", "a")
        arquivo1.write(f"{Price}")
        arquivo2 = open(fr"C:\Users\User\Desktop\TESTE\{VendedorName}\Descricao{sku}.txt", "a")
        arquivo2.write(f"{Description}")
    except TimeoutException:
        SkipPage = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Seguinte'))).click()
        sku -= 1
        y = 1
        x = 0
    # # # # CALCULAR O PREÇO # # # # #

   # if Preco < 50:
    ##    Preco =+ 15
     #   print(Preco)
    #elif Preco > 50:
     #   Preco += 20
      #  print(Preco)


   # print(Titulo)
   # print(Preco)
   # print(Descricao)
