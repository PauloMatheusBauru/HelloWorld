import pyperclip
import keyboard
import time

def Aplicações():
    ArquivoParaEscrita = open(R"C:\Users\User\Desktop\Teste.txt", "a")
    pyperclip.waitForNewPaste(print("Aguardando Marca(EX: TOYOTA)"))
    Marca = (pyperclip.paste())
    while True:
        pyperclip.waitForNewPaste(print("Aguardando Modelo(EX: YARIS)"))
        Modelo = (pyperclip.paste())
        pyperclip.waitForNewPaste(print("Aguardando Motor(EX: 1.3 16V)"))
        Motor = (pyperclip.paste())
        pyperclip.waitForNewPaste(print("Aguardando Ano(EX: 2003 A 2005)"))
        Ano = (pyperclip.paste())
        try:
            AnoInicial = (int(Ano[0:4]))
            AnoFinal = (int(Ano[-4:0]))
        except:
            AnoInicial = (int(Ano[0:4]))
            AnoFinal = AnoInicial + 3
        ListaAnos = (list(range(AnoInicial, AnoFinal)))
        ListaAnos = str(ListaAnos)
        pyperclip.waitForNewPaste(print("Aguardando Codigo do motor"))
        Codigo = (pyperclip.paste())
        ArquivoParaEscrita.write(f'\nMarca: {Marca};')
        ArquivoParaEscrita.write(f'\nModelo: {Modelo};')
        ArquivoParaEscrita.write(f'\nMotor: {Motor};')
        ArquivoParaEscrita.write(f'\nCodigo do motor: {Codigo};')
        ArquivoParaEscrita.write(f'\nAno: {ListaAnos[1:-1]}.')
        ArquivoParaEscrita.write("\n")
        print("Deseja Mudar de marca ou salvar pressione 'ESC' ou continue copiando")
        time.sleep(0.5)
        if keyboard.read_key() == 'esc':
            print("Selecione a outra marca")
            ArquivoParaEscrita.close()
            Aplicações()
        else:
            continue
Aplicações()