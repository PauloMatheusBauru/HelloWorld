from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pyperclip
import threading
import os
import fnmatch
from time import sleep
import re
import sqlite3
import smtplib
import win32com.client as win32

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('https://www.facebook.com/messages')
Email = browser.find_element_by_id('email')
Email.send_keys("paulom08@hotmail.com")
Senha = browser.find_element_by_xpath('//*[@id="pass"]')
Senha.send_keys("20012001")
Logar = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input')
Logar.click()

RespostaSim = ['sim', 'si', 'in', 'n', 's', 'si', 'si', 'im', 'm', 's', 'sin', 'n', 'din', 'dim']
RespostaNao = ['não', 'nao', 'n', 'na', 'ao' , 'no', 'nã', 'ão', 'nap', 'mao', 'mão']
Sair = ['sair', 'cancelar', 'parar', 'erro']
RespostaDinheiro = ['dinhei', 'dinheir', 'dinheiro', 'di', 'dinhe', 'dinhero', 'money', 'cash']
RespostaCartao = ['cartão', 'cartao', 'carta', 'catão', 'credito', 'debito', 'débito', 'artão', 'artao']

# criar a integração com o outlook
outlook = win32.Dispatch('outlook.application')

def deletar2():
    try:
        WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div[1]/div/a/div[1]/div[2]/div[2]/div/div/div/span')))
        ProcurarNovasMsg()
    except:
        try:
            print("Deletar")
            mousepontinhos = WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div[2]/div')))
            action = webdriver.ActionChains(browser)
            action.move_to_element(mousepontinhos)
            action.perform()
            selecionarpontinhos = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div[2]/div')))
            selecionarpontinhos.click()
            try:
                selecionardeletar = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div/div[1]/div/div[6]/div[2]/div')))
                selecionardeletar.click()
            except:
                selecionardeletar = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div/div[1]/div/div[3]/div[2]/div')))
                selecionardeletar.click()
            ConfirmarDelete = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[1]/div[1]')))
            ConfirmarDelete.click()
            Clientes.commit()
            ProcurarNovasMsg()
        except:
            ProcurarNovasMsg()

def deletar():
    mousepontinhos = WebDriverWait(browser, 1000000).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[1]/div[1]/div/a/div/div[2]/div[1]/div/div/div[1]/span/span/span/span')))
    action = webdriver.ActionChains(browser)
    action.move_to_element(mousepontinhos)
    action.perform()
    selecionarpontinhos = WebDriverWait(browser, 1000000).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[1]/div[2]/div')))
    selecionarpontinhos.click()
    try:
        selecionardeletar = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div/div[1]/div/div[6]/div[2]/div')))
        selecionardeletar.click()
    except:
        selecionardeletar = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div/div[1]/div/div[3]/div[2]/div')))
        selecionardeletar.click()
    ConfirmarDelete = WebDriverWait(browser, 1000000).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[1]/div[1]')))
    ConfirmarDelete.click()
    Clientes.commit()
    ProcurarNovasMsg()

def EntregaCartao():
    global ProdutoParavenda
    ProdutoParavenda = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]/div/a/div[1]/div[1]/div[2]/div/div[2]/span/span')))
    EntragaCadastroC = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    EntragaCadastroC.send_keys("Confira os dados para entrega: " + str(teste))
    print("Chegou até aqui")
    Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar.click()
    Clientes.commit()
    EntragaCadastroC1 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    EntragaCadastroC1.send_keys('Local de entrega está correto?  *"Sim"* Ou *"Não"*')
    Enviar1 = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar1.click()
    try:
        EntregaConfirmada = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[14]/div/div/div[2]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
        EntregaConfirmada = EntregaConfirmada.lower()
    except:
        EntregaConfirmada = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[15]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
        EntregaConfirmada = EntregaConfirmada.lower()

    if (EntregaConfirmada in RespostaSim):
        EntregaConfirm = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        EntregaConfirm.send_keys('Pedido efetuado com sucesso.  Entregas são efetuadas no seguinte horário: 8hrs Até 18hrs ' )
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        EnviarEmailCCadastro()
    elif (RespostaCadastro in RespostaNao):
        EntregaConfirm = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        EntregaConfirm.send_keys('Comece a conversa novamente. Ou se preferir entre em contato (XX)XXXX-XXXX')
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        deletar()
    elif (RespostaCadastro in Sair):
        EntregaConfirm = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        EntregaConfirm.send_keys('Obrigado por falar comigo. Até logo')
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        deletar()

def EntregaCadastroCartao():
    global ProdutoParavenda
    ProdutoParavenda = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]/div/a/div[1]/div[1]/div[2]/div/div[2]/span/span'))).text
    CpfCadastro = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[8]/div/div/div[2]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
    CadastroNovo = cursor.execute("SELECT * FROM clientes WHERE Cpf LIKE '" + str(CpfCadastro) + "';").fetchall()
    EntragaCadastroC = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    EntragaCadastroC.send_keys("Confira os dados para entrega: " + str(CadastroNovo))
    Clientes.commit()
    Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar.click()
    EntragaCadastroC1 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    EntragaCadastroC1.send_keys('Local de entrega está correto?  *"Sim"* Ou *"Não"*')
    Enviar1 = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar1.click()
    EntregaConfirmada = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[19]/div/div/div[2]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
    EntregaConfirmada = EntregaConfirmada.lower()
    if (EntregaConfirmada in RespostaSim):
        EntregaConfirm = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        EntregaConfirm.send_keys('Pedido efetuado com sucesso.  Entregas são efetuadas no seguinte horário: 8hrs Até 18hrs ' )
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        EnviarEmail2()
    elif (RespostaCadastro in RespostaNao):
        EntregaConfirm = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        EntregaConfirm.send_keys('Comece a conversa novamente. Ou se preferir entre em contato (XX)XXXX-XXXX')
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        EnviarEmail2()
    elif (RespostaCadastro in Sair):
        EntregaConfirm = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        EntregaConfirm.send_keys('Obrigado por falar comigo. Até logo')
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        deletar()
#Pergunta
def EntregaCadastro():
    global ProdutoParavenda
    ProdutoParavenda = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]/div/a/div[1]/div[1]/div[2]/div/div[2]/span/span'))).text
    global CadastroNovo
    CadastroNovo = cursor.execute("SELECT * FROM clientes WHERE Cpf LIKE '" + str(CpfCadastro) + "';").fetchall()
    try:
        Troco = WebDriverWait(browser, 13).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[19]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
    except:
        Troco = WebDriverWait(browser, 13).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[20]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
    EntragaCadastroC= WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    EntragaCadastroC.send_keys("Confira os dados para entrega: " + str(CadastroNovo))
    Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar.click()
    EntragaCadastroC1 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    EntragaCadastroC1.send_keys('Local de entrega está correto?  *"Sim"* Ou *"Não"*')
    Enviar1 = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar1.click()
    try:
        EntregaConfirmada = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[21]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
        EntregaConfirmada = EntregaConfirmada.lower()
    except:
        EntregaConfirmada = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[22]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
        EntregaConfirmada = EntregaConfirmada.lower()
    if (EntregaConfirmada in RespostaSim):
        EntregaConfirm = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        EntregaConfirm.send_keys('Pedido efetuado com sucesso.  Entregas são efetuadas no seguinte horário: 8hrs Até 18hrs ' )
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        EnviarEmailSCadastro()
    elif (RespostaCadastro in RespostaNao):
        EntregaConfirm = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        EntregaConfirm.send_keys('Comece a conversa novamente. Ou se preferir entre em contato (XX)XXXX-XXXX')
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        EnviarEmailSCadastro()

def Entrega():
    global ProdutoParavenda
    ProdutoParavenda = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]/div/a/div[1]/div[1]/div[2]/div/div[2]/span/span'))).text
    try:
        Troco = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[12]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
    except:
        Troco = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[13]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
    EntregaConfirm2 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    EntregaConfirm2.send_keys("Confira os dados para entrega: " + str(teste))
    Enviar = browser.find_element_by_xpath( '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar.click()
    EntregaConfirm3 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    EntregaConfirm3.send_keys('Local de entrega está correto?  *"Sim"* Ou *"Não"*')
    Enviar1 = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar1.click()
    try:
        EntregaConfirmada = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[16]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
        EntregaConfirmada = EntregaConfirmada.lower()
    except:
        EntregaConfirmada = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[17]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
        EntregaConfirmada = EntregaConfirmada.lower()
    if (EntregaConfirmada in RespostaSim):
        EntregaConfirm = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        EntregaConfirm.send_keys('Pedido efetuado com sucesso.  Entregas são efetuadas no seguinte horário: 8hrs Até 18hrs ' )
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        EnviarEmailCCadastro()
    elif (RespostaCadastro in RespostaNao):
        EntregaConfirm = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        EntregaConfirm.send_keys('Endereço cadastrado está errado? Entre em contato: (XX)XXXX-XXXX')
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        ProcurarNovasMsg()

def FormaPagamento2():
    FormaDePagamento = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    FormaDePagamento.send_keys('Forma de Pagamento: *"Dinheiro"* ou *"Cartão"*')
    Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar.click()
    try:
        FormaPagamentoResposta = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[17]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
        FormaPagamentoResposta = FormaPagamentoResposta.lower()
    except:
        FormaPagamentoResposta = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[18]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
        FormaPagamentoResposta = FormaPagamentoResposta.lower()
    if (FormaPagamentoResposta in RespostaDinheiro):
        TrocoPara = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        TrocoPara.send_keys('Você escolheu dinheiro. Troco para quanto?')
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        EntregaCadastro()
    elif (FormaPagamentoResposta in RepostaCartao):
        print("Chegou aqui")
        FormaPagamentoCartao = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        FormaPagamentoCartao.send_keys('Você escolheu cartão!')
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        EntregaCadastroCartao()

def FormaPagamento():
    FormaDePagamento = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    FormaDePagamento.send_keys('Forma de Pagamento: *"Dinheiro"* ou *"Cartão"*')
    Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar.click()
    try:
        FormaPagamentoResposta = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[10]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
        FormaPagamentoResposta = FormaPagamentoResposta.lower()
    except:
        FormaPagamentoResposta = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[11]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
        FormaPagamentoResposta = FormaPagamentoResposta.lower()
    if (FormaPagamentoResposta in RespostaDinheiro):
        TrocoPara = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        TrocoPara.send_keys('Você escolheu dinheiro.Troco para quanto?')
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        Entrega()
    elif (FormaPagamentoResposta in RespostaCartao):
        print("Firma")
        FormaPagamentoCartao = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        FormaPagamentoCartao.send_keys('Você escolheu cartão!')
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        EntregaCartao()

def Responder():
    print("Sem opçao automatica")
    ChatEtapa1 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    ChatEtapa1.send_keys('Olá, Eu sou um robo de compra irei te fazer algumas perguntas, me responda com 1 palavra por vez. Você deseja comprar este item? Digite "Sim" Ou "Não" Caso queira cancelar a compra digite "Sair"')
    Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar.click()
    RespostaComprar = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[4]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
    RespostaComprar = RespostaComprar.lower()
    if (RespostaComprar in RespostaSim):
        ChatEtapa2 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        ChatEtapa2.send_keys('Já Possui Cadastro ? "Sim" Ou "Não"')
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        RespostaCadastro = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[6]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
        RespostaCadastro = RespostaCadastro.lower()
        if (RespostaCadastro in RespostaSim):
            ChatEtapa3 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
            ChatEtapa3.send_keys('Digite Seu "CPF" para localizarmos em nosso cadastro')
            Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
            Enviar.click()
            try:
                CpfCadastroefetuado = WebDriverWait(browser, 25).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[8]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
            except:
                CpfCadastroefetuado = WebDriverWait(browser, 25).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[9]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
            global teste
            teste = cursor.execute("SELECT * FROM clientes WHERE Cpf LIKE '" + str(CpfCadastroefetuado) + "';").fetchall()
            FormaPagamento()
        elif (RespostaCadastro in RespostaNao):
            ChatEtapa3 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
            ChatEtapa3.send_keys('Digite Seu "CPF" para iniciar o cadastro')
            Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
            Enviar.click()
            global CpfCadastro
            try:
                CpfCadastro = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[8]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
                ChatEtapa3 = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
            except:
                CpfCadastro = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[9]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
                ChatEtapa3 = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
            ChatEtapa3.send_keys('Digite Seu nome completo, Exemplo: Pedro Álvares Cabral')
            Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
            Enviar.click()
            try:
                NomeCliente = WebDriverWait(browser, 25).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[10]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
                ChatEtapa3 = WebDriverWait(browser, 25).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
            except:
                NomeCliente = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[11]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
                ChatEtapa3 = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
            ChatEtapa3.send_keys('Digite Endereço, exemplo: *Rua Alberto Del Masso XXXX*')
            Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
            Enviar.click()
            try:
                EnderecoCadastro = WebDriverWait(browser, 22).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[12]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
                ChatEtapa3 = WebDriverWait(browser, 22).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
            except:
                EnderecoCadastro = WebDriverWait(browser, 22).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[13]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
                ChatEtapa3 = WebDriverWait(browser, 22).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
            ChatEtapa3.send_keys('Digite Seu telefone Exemplo: *1496430XXXX*')
            Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
            Enviar.click()
            try:
                TelefoneCadastro = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[14]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
            except:
                TelefoneCadastro = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[15]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
            ChatEtapa3 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
            ChatEtapa3.send_keys('Dados Cadastrados: '+ NomeCliente + " " + CpfCadastro + " " + EnderecoCadastro + " " + TelefoneCadastro)
            Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
            Enviar.click()
            cursor.execute("INSERT INTO clientes VALUES ('" +str(NomeCliente)+"', '" + str(CpfCadastro) + "', '" + str(TelefoneCadastro) + "', '" + str(EnderecoCadastro) + "')")
            Clientes.commit()
            FormaPagamento2()

################## COM RESPONDER SOZINHO#################################################
################## COM RESPONDER SOZINHO#################################################
################## COM RESPONDER SOZINHO#################################################
################## COM RESPONDER SOZINHO#################################################
################## COM RESPONDER SOZINHO#################################################
################## COM RESPONDER SOZINHO#################################################
################## COM RESPONDER SOZINHO#################################################
################## COM RESPONDER SOZINHO#################################################
################## COM RESPONDER SOZINHO#################################################
################## COM RESPONDER SOZINHO#################################################
################## COM RESPONDER SOZINHO#################################################
################## COM RESPONDER SOZINHO#################################################
################## COM RESPONDER SOZINHO#################################################
################## COM RESPONDER SOZINHO#################################################
################## COM RESPONDER SOZINHO#################################################
################## COM RESPONDER SOZINHO#################################################
################## COM RESPONDER SOZINHO#################################################



def EntregaScadastroCartaoB():
    global ProdutoParavenda
    ProdutoParavenda = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]/div/a/div[1]/div[1]/div[2]/div/div[2]/span/span'))).text
    CpfCadastro = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[10]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
    global CadastroNovo
    CadastroNovo = cursor.execute("SELECT * FROM clientes WHERE Cpf LIKE '" + str(CpfCadastro) + "';").fetchall()
    EntragaCadastroC = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    EntragaCadastroC.send_keys("Confira os dados para entrega: " + str(CadastroNovo))
    Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar.click()
    EntragaCadastroC1 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    EntragaCadastroC1.send_keys('Local de entrega está correto?  *"Sim"* Ou *"Não"*')
    Enviar1 = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar1.click()
    EntregaConfirmada = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[21]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
    EntregaConfirmada = EntregaConfirmada.lower()
    if (EntregaConfirmada in RespostaSim):
        EntregaConfirm = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        EntregaConfirm.send_keys('Pedido efetuado com sucesso.  Entregas são efetuadas no seguinte horário: 8hrs Até 18hrs ' )
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        EnviarEmailSCadastro()
    elif (RespostaCadastro in RespostaNao):
        EntregaConfirm = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        EntregaConfirm.send_keys('Comece a conversa novamente. Ou se preferir entre em contato (XX)XXXX-XXXX')
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        deletar()

def EntregaCcadastroCartaoB():
    global ProdutoParavenda
    ProdutoParavenda = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]/div/a/div[1]/div[1]/div[2]/div/div[2]/span/span'))).text
    CpfCadastro = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[11]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
    global teste
    teste = cursor.execute("SELECT * FROM clientes WHERE Cpf LIKE '" + str(CpfCadastro) + "';").fetchall()
    EntragaCadastroC = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    EntragaCadastroC.send_keys("Confira os dados para entrega: " + str(teste))
    Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar.click()
    EntragaCadastroC1 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    EntragaCadastroC1.send_keys('Local de entrega está correto?  *"Sim"* Ou *"Não"*')
    Enviar1 = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar1.click()
    EntregaConfirmada = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[18]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
    EntregaConfirmada = EntregaConfirmada.lower()
    if (EntregaConfirmada in RespostaSim):
        EntregaConfirm = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        EntregaConfirm.send_keys('Pedido efetuado com sucesso.  Entregas são efetuadas no seguinte horário: 8hrs Até 18hrs ' )
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        EnviarEmailCCadastro()
    elif (EntregaConfirmada in RespostaNao):
        EntregaConfirm = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        EntregaConfirm.send_keys('Comece a conversa novamente. Ou se preferir entre em contato (XX)XXXX-XXXX')
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        ProcurarNovasMsg()

#Pergunta
def EntregaCadastroB():
    global ProdutoParavenda
    ProdutoParavenda = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]/div/a/div[1]/div[1]/div[2]/div/div[2]/span/span'))).text
    global CadastroNovo
    CpfCadastro = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[11]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
    CadastroNovo = cursor.execute("SELECT * FROM clientes WHERE Cpf LIKE '" + str(CpfCadastro) + "';").fetchall()
    Troco = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[21]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
    EntragaCadastroC= WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    EntragaCadastroC.send_keys("Confira os dados para entrega: " + str(CadastroNovo))
    Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar.click()
    EntragaCadastroC1 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    EntragaCadastroC1.send_keys('Local de entrega está correto?  *"Sim"* Ou *"Não"*')
    Enviar1 = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar1.click()
    EntregaConfirmada = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[21]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
    EntregaConfirmada = EntregaConfirmada.lower()
    if (EntregaConfirmada in RespostaSim):
        EntregaConfirm = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        EntregaConfirm.send_keys('Pedido efetuado com sucesso.  Entregas são efetuadas no seguinte horário: 8hrs Até 18hrs ' )
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        EnviarEmailSCadastro()
    elif (EntregaConfirmada in RespostaNao):
        EntregaConfirm = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        EntregaConfirm.send_keys('Comece a conversa novamente. Ou se preferir entre em contato (XX)XXXX-XXXX')
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        ProcurarNovasMsg()



def EntregaB():
    global ProdutoParavenda
    ProdutoParavenda = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]/div/a/div[1]/div[1]/div[2]/div/div[2]/span/span'))).text
    global teste
    Troco = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[15]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
    EntregaConfirm2 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    EntregaConfirm2.send_keys("Confira os dados para entrega: " + str(teste))
    Enviar = browser.find_element_by_xpath( '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar.click()
    EntregaConfirm3 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    EntregaConfirm3.send_keys('Local de entrega está correto?  *"Sim"* Ou *"Não"*')
    Enviar1 = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar1.click()
    EntregaConfirmada = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[18]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
    EntregaConfirmada = EntregaConfirmada.lower()
    if (EntregaConfirmada in RespostaSim):
        EntregaConfirm = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        EntregaConfirm.send_keys('Pedido efetuado com sucesso.  Entregas são efetuadas no seguinte horário: 8hrs Até 18hrs ' )
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        EnviarEmailCCadastro()
    elif (EntregaConfirmada in RespostaNao):
        EntregaConfirm = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        EntregaConfirm.send_keys('Endereço cadastrado está errado? Entre em contato: (XX)XXXX-XXXX')
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        ProcurarNovasMsg()

def FormaPagamento2B():
    FormaDePagamento = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    FormaDePagamento.send_keys('Forma de Pagamento: *"Dinheiro"* ou *"Cartão"*')
    Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar.click()
    FormaPagamentoResposta = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[20]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
    FormaPagamentoResposta = FormaPagamentoResposta.lower()
    if (FormaPagamentoResposta in RespostaDinheiro):
        TrocoPara = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        TrocoPara.send_keys('Você escolheu dinheiro. Troco para quanto?')
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        EntregaCadastroB()
    elif (FormaPagamentoResposta in RespostaCartao):
        FormaPagamentoCartao = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        FormaPagamentoCartao.send_keys('Você escolheu cartão!')
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        EntregaScadastroCartaoB()

def FormaPagamentoB():
    FormaDePagamento2 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    FormaDePagamento2.send_keys('Forma de Pagamento: *"Dinheiro"* ou *"Cartão"*')
    Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar.click()
    FormaPagamentoResposta2 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[13]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
    FormaPagamentoResposta2 = FormaPagamentoResposta2.lower()
    if (FormaPagamentoResposta2 in RespostaDinheiro):
        TrocoPara = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        TrocoPara.send_keys('Você escolheu dinheiro.Troco para quanto?')
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        EntregaB()
    elif (FormaPagamentoResposta2 in RespostaCartao):
        FormaPagamentoCartao2 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        FormaPagamentoCartao2.send_keys('Você escolheu cartão!')
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        EntregaCcadastroCartaoB()

def ResponderB():
    print("Responder Com botao")
    ChatEtapa1 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
    ChatEtapa1.send_keys('Olá, Eu sou um robo de compra irei te fazer algumas perguntas, me responda com 1 palavra por vez. Você deseja comprar este item? Digite "Sim" Ou "Não" Caso queira cancelar a compra digite "Sair"')
    Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
    Enviar.click()
    RespostaComprar = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[6]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
    RespostaComprar = RespostaComprar.lower()
    if (RespostaComprar in RespostaSim):
        ChatEtapa2 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
        ChatEtapa2.send_keys('Já Possui Cadastro ? "Sim" Ou "Não"')
        Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        Enviar.click()
        RespostaCadastro = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[9]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
        RespostaCadastro = RespostaCadastro.lower()
        if (RespostaCadastro in RespostaSim):
            ChatEtapa3 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
            ChatEtapa3.send_keys('Digite Seu "CPF" para localizarmos em nosso cadastro')
            Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
            Enviar.click()
            CpfCadastroefetuado = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[11]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
            global teste
            teste = cursor.execute("SELECT * FROM clientes WHERE Cpf LIKE '" + str(CpfCadastroefetuado) + "';").fetchall()
            FormaPagamentoB()
        elif (RespostaCadastro in RespostaNao):
            ChatEtapa3 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
            ChatEtapa3.send_keys('Digite Seu "CPF" para iniciar o cadastro')
            Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
            Enviar.click()
            global CpfCadastro
            CpfCadastro = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[11]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
            ChatEtapa3 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
            ChatEtapa3.send_keys('Digite Seu nome completo, Exemplo: Pedro Álvares Cabral')
            Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
            Enviar.click()
            NomeCliente = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[13]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
            ChatEtapa3 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
            ChatEtapa3.send_keys('Digite Endereço, exemplo: *Rua Alberto Del Masso XXXX*')
            Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
            Enviar.click()
            EnderecoCadastro = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[15]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
            ChatEtapa3 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
            ChatEtapa3.send_keys('Digite Seu telefone Exemplo: *1496430XXXX*')
            Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
            Enviar.click()
            TelefoneCadastro = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[17]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div[1]/div/div'))).text
            ChatEtapa3 = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
            ChatEtapa3.send_keys('Dados Cadastrados: '+ NomeCliente + " " + CpfCadastro + " " + EnderecoCadastro + " " + TelefoneCadastro)
            Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
            Enviar.click()
            cursor.execute("INSERT INTO clientes VALUES ('" +str(NomeCliente)+"', '" + str(CpfCadastro) + "', '" + str(TelefoneCadastro) + "', '" + str(EnderecoCadastro) + "')")
            Clientes.commit()
            FormaPagamento2B()
        elif (RespostaCadastro in Sair):
            EntregaConfirm = WebDriverWait(browser, 240).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div')))
            EntregaConfirm.send_keys('Obrigado por falar comigo. Até logo')
            Enviar = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
            Enviar.click()
            ProcurarNovasMsg()


def tembotao():
    try:
        if WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[4]/div/div/div[1]/div[2]/div[1]/div[1]/span/div/div/div/div/div/div/div[2]/div[1]/span/div/div/div[2]'))):
            ResponderB()
    except:
        Responder()

def ProcurarNovasMsg():
    i = 1
    sleep(2)
    while True:
        try:
            print("TRY")
            print(i)
            if WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[' + str(i) + ']/div/a/div[1]/div[2]/div[2]/div/div/div/span'))):
                print("Localizado")
                Notificacao = WebDriverWait(browser, 9999999999999).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/div/div[' + str(i) + ']')))
                Notificacao.click()
                sleep(3)
                tembotao()
        except:
            i += 1
            if i == 4:
                i = 1
                deletar2()
Clientes = sqlite3.connect('clientes.db')

cursor = Clientes.cursor()
def clicarMarketPlace():
    try:
        MarketPlace = WebDriverWait(browser, 10000000000000).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[1]')))
        MarketPlace.click()
        ProcurarNovasMsg()
    except:
        clicarMarketPlace()


def EnviarEmailCCadastro():
    email = outlook.CreateItem(0)

    # configurar as informações do seu e-mail
    email.To = "paulom12345@hotmail.com"
    email.Subject = "E-mail automático do Python"
    email.HTMLBody = f"""
    <p>Olá (Empresa), um usuario quer comprar o item</p>
    <p>{ProdutoParavenda}</p>
    <p>Dados para confirmar compra</p>
    <p>{teste}</p>
    <p>Abs,</p>
    <p>Código Python</p>
    """

    # anexo = "C://Users/joaop/Downloads/arquivo.xlsx"
    # email.Attachments.Add(anexo)

    email.Send()
    print("Email Enviado")


def EnviarEmailSCadastro():
    email = outlook.CreateItem(0)
    faturamento = 1500
    qtde_produtos = 10
    ticket_medio = faturamento / qtde_produtos

    # configurar as informações do seu e-mail
    email.To = "paulom12345@hotmail.com"
    email.Subject = "E-mail automático do Python"
    email.HTMLBody = f"""
    <p>Olá (Empresa), um usuario quer comprar o item</p>
    <p>{ProdutoParavenda}</p>
    <p>Dados para confirmar compra</p>
    <p>{CadastroNovo}</p>
    <p>Abs,</p>
    <p>Código Python</p>
    """

    # anexo = "C://Users/joaop/Downloads/arquivo.xlsx"
    # email.Attachments.Add(anexo)

    email.Send()
    print("Email Enviado")


clicarMarketPlace()
# Copyright 2021, Paulo Matheus Rodrigues, All rights reserved