import time

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard, MDCardSwipe
from kivymd.uix.snackbar import Snackbar
import ssl
from kivy.loader import Loader
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivy.clock import Clock
from kivymd.uix.spinner import MDSpinner
import requests
import re
import ast
import webbrowser
from kivyoav.delayed import delayable
from kivymd.toast import toast
import json
#
Builder.load_file("my.kv")


NomeProdutoDescrição = ""
ImgDescrição = ""
DescricaoProduto = ""
Carrinho = {}
ValorCestinha = 0
Sku = ""
PrecoAtualizado = 0




class ConfirmarCompra(Screen):
    NomeCompleto = StringProperty()
    Email = StringProperty()
    Cep = StringProperty()
    NumeroResidencia = StringProperty()
    Cpf = StringProperty()
    EnderecoEntrega = StringProperty()
    pass

class Logado(BoxLayout, Screen):
    NomeCompleto = StringProperty()
    Email = StringProperty()
    Cep = StringProperty()
    NumeroResidencia = StringProperty()
    Cpf = StringProperty()
    EnderecoEntrega = StringProperty()
    pass


class SettingsConta(Screen):
    NomeCompleto = StringProperty()
    Email = StringProperty()
    Cep = StringProperty()
    NumeroResidencia = StringProperty()
    Cpf = StringProperty()
    EnderecoEntrega = StringProperty()
    pass

class ProdutosCarrinho(MDCardSwipe, RoundedRectangularElevationBehavior, MDApp):
    Titulo = StringProperty()
    Preco = StringProperty()
    Img = StringProperty()
    Sku = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global ValorCestinha
        self.Quantidade = 1
        ValorCestinha += float(self.Preco[3:])
        print(ValorCestinha)


    def Add(self, *args):
        global ValorCestinha
        self.Quantidade += 1
        print(self.Quantidade, self.Titulo)
        ValorCestinha += float(self.Preco[3:])
        print(f"Valor Total: {ValorCestinha:,.2f}")
        Carrinho[f'{self.Sku}'] = self.Quantidade
        self.ids.QuantidadeProdutos.text = str(self.Quantidade)

    def Remove(self, *args):
        if self.Quantidade <= 1:
            pass
        else:
            global ValorCestinha
            self.Quantidade -= 1
            print(self.Quantidade, self.Titulo)
            ValorCestinha -= float(self.Preco[3:])
            print(f"Valor Total: {ValorCestinha:,.2f}")
            Carrinho[f'{self.Sku}'] = self.Quantidade
            self.ids.QuantidadeProdutos.text = str(self.Quantidade)

    def RemoverCarrinho(self):
        try:
            global ValorCestinha
            RemoverValorCestinha = self.Quantidade * float(self.Preco[3:])
            print(RemoverValorCestinha)
            ValorCestinha -= RemoverValorCestinha
            del Carrinho[f'{self.Sku}']
            self.Quantidade = 0
            print(format(ValorCestinha, '.2f'))
        except:
            pass

class SpinnerPaulo(MDSpinner):
    pass

class MD2Card(MDCard):
    pass

class MD3Card(MDCard):
    '''Implements a material design v3 card.'''
    UrlImagem = StringProperty()
    Titulo = StringProperty()
    Preco = StringProperty()
    Sku = StringProperty()
    DescricaoProduto = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_show(self, instance, new_obj):
        # handle the ObjectProperty named show
        if new_obj.parent:
            # remove this obj from any other MyObject instance
            new_obj.parent.remove_widget(new_obj)
        for ch in self.children:
            if isinstance(ch, Image):
                # remove any previous obj instances
                self.remove_widget(ch)
                break
        # add the new obj to this MyObject instance
        self.add_widget(new_obj)

    def InformacoesAtt(self):
        global NomeProdutoDescrição
        global ImgDescrição
        global DescricaoProduto
        global Sku
        global PrecoAtualizado
        NomeProdutoDescrição = self.Titulo
        ImgDescrição = self.UrlImagem
        DescricaoProduto = self.DescricaoProduto
        Sku = self.Sku
        self.Preco = re.sub(",", ".", self.Preco)
        PrecoAtualizado = self.Preco[2:]


class MainWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class InfoItem(Screen):
    pass

class Cadastrar(Screen):
    pass

class Pedidos(Screen):
    pass

class OrdemPedido(MDCard, MDApp):
    '''Implements a material design v3 card.'''
    IDPedido = StringProperty()
    Despachado = StringProperty()
    Produtos = StringProperty()

    def Cancelamento(self):
        print(self.IDPedido)
        print(self.Status)
        print(self.Despachado)
        SendMsg = "EnviarCance:" + str(self.IDPedido)
        client.sendall(bytes(SendMsg, 'UTF-8'))
        in_data = client.recv(2780)
        Recebido = in_data.decode()
        print(Recebido)
        if Recebido == "Ok":
            toast("Pedido enviado para cancelamento aguarde contato do vendedor")
        elif Recebido == "Erro":
            toast("Houve algum erro")
        elif Recebido == "Devolução":
            toast("Produto já enchaminhado para devolução aguarde contato")

    def TrocaProdutoComDefeito(self):
        print(self.IDPedido)
        print(self.Status)
        print(self.Despachado)
        SendMsg = "EnviarDefei:" + str(self.IDPedido)
        client.sendall(bytes(SendMsg, 'UTF-8'))
        in_data = client.recv(2780)
        Recebido = in_data.decode()
        print(Recebido)
        if Recebido == "Ok":
            toast("Pedido enviado para TROCA aguarde contato do vendedor")
        elif Recebido == "Erro":
            toast("Houve algum erro")
        elif Recebido == "Devolução":
            toast("Produto já enchaminhado para devolução aguarde contato")


class MainApp(MDApp):
    Connected = False

    def build_config(self, config):
        config.setdefaults('login', {'username': '', 'password': ''})

    def GoogleMaps(self):
        webbrowser.open("https://www.google.com.br/maps/place/Paran%C3%A1+Auto+Pe%C3%A7as/@-22.3138799,-49.073397,17z/data=!3m1!4b1!4m5!3m4!1s0x94bf67b82f4fe4ed:0x26bea39a1f2539dc!8m2!3d-22.3138849!4d-49.071203?hl=pt-BR")

    def build(self):
        self.Pesquisou = False
        self.sm = ScreenManager()
        self.sm.add_widget(MainWindow(name = "MainWindow"))
        self.sm.add_widget(InfoItem(name = "InfoItem"))
        self.sm.add_widget(Logado(name="Logado"))
        self.sm.add_widget(Cadastrar(name="Cadastrar"))
        self.sm.add_widget(SettingsConta(name="SettingsConta"))
        self.sm.add_widget(Pedidos(name="Pedidos"))
        self.sm.add_widget(ConfirmarCompra(name="ConfirmarCompra"))
        return self.sm

    def on_start(self):
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)
        config = self.config
        self.username = config.get('login', 'username')
        self.password = config.get('login', 'password')
        self.root.get_screen("MainWindow").ids.Email.text = self.username
        self.root.get_screen("MainWindow").ids.Senha.text = self.password
        print(self.username)

    def hook_keyboard(self, window, key, *largs):
        if key == 27:
            self.sm.current = "MainWindow"
            self.root.get_screen("MainWindow").ids.tabs.switch_tab("Compra")
            return True

    def AtualizarValores(self, *args):
        self.ValorTotal = str(format(ValorCestinha, '.2f'))
        self.root.get_screen("MainWindow").ids.TotalCarrinho.text = str(f"R$ {self.ValorTotal}")
        print("A")

    def AtualizarValoresDescrição(self):
        self.root.get_screen("InfoItem").ids.teste.text = str(f"{NomeProdutoDescrição}")
        self.root.get_screen("InfoItem").ids.ImgTrocar.source = str(f"{ImgDescrição}")
        self.root.get_screen("InfoItem").ids.DescricaoInfo.text = str(f"{DescricaoProduto}")


    def Pesquisar(self):
        self.root.get_screen("MainWindow").ids.box.opacity = 0
        if self.Pesquisou == False:
            self.Pesquisou = True
            try:
                self.root.get_screen("MainWindow").ids.Compra.remove_widget(self.root.get_screen("MainWindow").ids.MD2Card)
            except:
                pass
            self.Spinner = SpinnerPaulo()
            self.root.get_screen("MainWindow").ids.Compra.add_widget(self.Spinner)
            Clock.schedule_once(self.Pesquisar1, 0)
            self.root.get_screen("MainWindow").ids.box.clear_widgets()
        else:
            pass

    def Lampadas(self):
        self.root.get_screen("MainWindow").ids.box.opacity = 0
        if self.Pesquisou == False:
            self.Pesquisou = True
            try:
                self.root.get_screen("MainWindow").ids.Compra.remove_widget(self.root.get_screen("MainWindow").ids.MD2Card)
            except:
                pass
            self.Spinner = SpinnerPaulo()
            self.root.get_screen("MainWindow").ids.Compra.add_widget(self.Spinner)
            self.root.get_screen("MainWindow").ids.Pesquisar.text = "Lampada"
            Clock.schedule_once(self.Pesquisar1, 0)
            self.root.get_screen("MainWindow").ids.box.clear_widgets()
        else:
            pass

    def OrdemPedidos(self):
        self.root.get_screen("Pedidos").ids.rvPedidos.data = []
        SendMsg = "OrdemPedidos:" + str(self.Cpf)
        client.sendall(bytes(SendMsg, 'UTF-8'))
        while True:
            in_data = client.recv(1600)
            Recebido = in_data.decode()
            print(Recebido)
            if Recebido == "fim":
                break
            Recebido = ast.literal_eval(Recebido)
            SendMsg = "Ok"
            client.send(bytes(SendMsg, 'UTF-8'))
            self.ID = Recebido['IDPedido']
            self.Despachado = Recebido['Despachado']
            self.Status = Recebido['Status']
            if self.Status == "Aprovado":
                self.root.get_screen("Pedidos").ids.rvPedidos.data.append(
                    {'IDPedido': "ID Compra: " + str(self.ID), 'Despachado': str(self.Despachado), 'Status': str(self.Status)})
                SendMsg = "Ok"
                client.send(bytes(SendMsg, 'UTF-8'))
            elif self.Status == "Devolução":
                self.root.get_screen("Pedidos").ids.rvPedidos.data.append(
                    {'IDPedido': "ID Compra: " + str(self.ID), 'Despachado': str(self.Despachado), 'Status': str(self.Status)})
                SendMsg = "Ok"
                client.send(bytes(SendMsg, 'UTF-8'))
            else:
                pass


    @delayable
    def Pesquisar1(self, *args):
        yield 0.03
        Count = 0
        Pesquisa = self.root.get_screen("MainWindow").ids.Pesquisar.text
        self.root.get_screen("MainWindow").ids.rv.data = []
        data = requests.get(f"http://51.161.100.2:8080/search/{Pesquisa}")
        data = data.json()
        for self.Produtos in data:
            self.TituloProduto = self.Produtos['Title']
            self.UrlImagem = self.Produtos['UrlImage']
            self.ValorProduto = self.Produtos['ProductPrice']
            self.Sku = self.Produtos['Sku']
            self.Descricao = "A"
            Count += 1
            yield 0.03
            self.root.get_screen("MainWindow").ids.rv.data.append(
                {'Titulo': str(self.TituloProduto), 'UrlImagem': str(self.UrlImagem),
                 'Preco': "R$ " + str(self.ValorProduto),
                 'Sku': str(self.Sku),
                 'DescricaoProduto': str(self.Descricao)})
            if Count == 20:
                self.root.get_screen("MainWindow").ids.box.opacity = 1
                self.Pesquisou = False
                self.root.get_screen("MainWindow").ids.Compra.remove_widget(self.Spinner)
            else:
                pass
        try:
            self.root.get_screen("MainWindow").ids.box.opacity = 1
            self.Pesquisou = False
            self.root.get_screen("MainWindow").ids.Compra.remove_widget(self.Spinner)
        except:
            pass

    def AddCart(self):
        self.Carrinho = Carrinho
        if (Sku in self.Carrinho) == False:
            self.Carrinho[f'{Sku}'] = 1
            toast(f"Produto Adiconado Ao Carrinho")
            self.Produtos = ProdutosCarrinho(Titulo=f"{NomeProdutoDescrição}", Preco=f"R$ {PrecoAtualizado}",Img=f'{ImgDescrição}', Sku=f'{Sku}')
            self.sm.current = "MainWindow"
            self.root.get_screen("MainWindow").ids.tabs.switch_tab("Finalizar Pedido")
            Clock.schedule_once(self.AddItemCart, 0.1)
            print(Carrinho)
        else:
            pass

    def ConfirmarDadosPagamento(self):
        if self.Connected == False:
            print("Não Logado")
            pass
        else:
            self.root.get_screen("ConfirmarCompra").ids.NomeCompletoLogado.text = self.NomeCompleto
            self.root.get_screen("ConfirmarCompra").ids.Cpf.text = self.Cpf
            self.root.get_screen("ConfirmarCompra").ids.EmailLogado.text = self.Email
            self.root.get_screen("ConfirmarCompra").ids.NumeroResidencia.text = self.NumeroResidencia
            self.root.get_screen("ConfirmarCompra").ids.Cep.text = self.Cep
            self.sm.current = "ConfirmarCompra"

    @delayable
    def AddItemCart(self, *args):
        yield 0.05
        self.root.get_screen("MainWindow").ids.ProdutosCarrinho.add_widget(self.Produtos)

    def RemoverCarrinho(self, instance):
        self.root.get_screen("MainWindow").ids.ProdutosCarrinho.remove_widget(instance)

    def Logar(self):
        self.Email = self.root.get_screen("MainWindow").ids.Email.text
        self.Senha = self.root.get_screen("MainWindow").ids.Senha.text
        self.config.set('login', 'username', self.Email)
        self.config.set('login', 'password', self.Senha)
        self.config.write()
        data = {
            'Email': f'{self.Email}',
            'Senha': f'{self.Senha}',
        }
        url = "http://192.168.1.163:5000/Cubagem"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        self.Cpf = RequestLogin['Cpf']
        self.NomeCompleto = RequestLogin['NomeCompleto']
        self.Cep = RequestLogin['Cep']
        self.Telefone = RequestLogin['Telefone']
        self.NumeroResidencia = RequestLogin['NumeroResidencia']
        self.Email = RequestLogin['Email']
        self.SenhaBd = RequestLogin['SenhaBd']
        if self.Senha == self.SenhaBd:
            # print("Logado")
            # print(f"{self.Cpf},{self.NomeCompleto},{self.Email}")
            self.root.current = "Logado"
            self.root.get_screen("MainWindow").ids.tabs.switch_tab("Compra")
            self.root.get_screen("SettingsConta").ids.NomeCompletoLogado.text = self.NomeCompleto
            self.root.get_screen("SettingsConta").ids.Cpf.text = self.Cpf
            self.root.get_screen("SettingsConta").ids.EmailLogado.text = self.Email
            self.root.get_screen("SettingsConta").ids.NumeroResidencia.text = self.NumeroResidencia
            self.root.get_screen("SettingsConta").ids.Cep.text = self.Cep
            self.Connected = True
            print(self.Connected)
        else:
            print("Senha Incorreta")

    def EditarConta(self):
        self.sm.current = "SettingsConta"


    def Pedidos(self):
        self.sm.current = "Pedidos"


    def Create_Account(self, *args):
        self.NomeCompleto = self.root.get_screen("Cadastrar").ids.Nome.text
        self.Email = self.root.get_screen("Cadastrar").ids.Email.text
        self.Senha = self.root.get_screen("Cadastrar").ids.Senha.text
        self.Telefone = self.root.get_screen("Cadastrar").ids.Telefone.text
        self.Cep = self.root.get_screen("Cadastrar").ids.Cep.text
        self.Cpf = self.root.get_screen("Cadastrar").ids.Cpf.text
        self.NumeroResidencia = self.root.get_screen("Cadastrar").ids.NumeroCasa.text
        if self.NomeCompleto == "":
            self.snackbar = Snackbar(text="Nome não preenchido")
            self.snackbar.open()
        elif self.Email == "":
            self.snackbar = Snackbar(text="Email não preenchido")
            self.snackbar.open()
        elif self.Senha == "":
            self.snackbar = Snackbar(text="Senha não preenchido")
            self.snackbar.open()
        elif self.Telefone == "":
            self.snackbar = Snackbar(text="Telefone não preenchido")
            self.snackbar.open()
        elif self.Cep == "":
            self.snackbar = Snackbar(text="Cep não preenchido")
            self.snackbar.open()
        elif self.Cpf == "":
            self.snackbar = Snackbar(text="Cpf não preenchido")
            self.snackbar.open()
        elif len(self.Cpf) <= 10:
            self.snackbar = Snackbar(text="Cpf Faltando Numeros")
            self.snackbar.open()
        elif self.NumeroResidencia == "":
            self.snackbar = Snackbar(text="Numero Residência não preenchido")
            self.snackbar.open()
        else:
            d = {
                'NomeCompleto': f'{self.NomeCompleto}',
                'Email': f'{self.Email}',
                'Senha': f'{self.Senha}',
                'Telefone': f'{self.Telefone}',
                'Cpf': f'{self.Cpf}',
                'NumeroResidencia': f'{self.NumeroResidencia}',
                'Cep': f'{self.Cep}',
            }
            SendMsg = "Cadastrar:" + str(d)
            client.send(bytes(SendMsg, 'UTF-8'))
            in_data = client.recv(1024)
            Recebido = in_data.decode()
            if Recebido == "Ok":
                toast("Cadastro efetuado com sucesso")
                self.root.current = "MainWindow"
            else:
                toast("Erro")

    def Voltar(self):
        self.root.current = "MainWindow"
        self.root.get_screen("MainWindow").ids.tabs.switch_tab("Compra")

    def Deslogar(self):
        self.root.current = "MainWindow"
        self.Connected = False

    def VoltarInicial(self):
        self.root.get_screen("MainWindow").ids.tabs.switch_tab("Compra")
        self.root.current = "MainWindow"

    def VerificarLogado(self):
        print(self.Connected)
        if self.Connected == True:
            try:
                self.root.current = "Logado"
                self.root.get_screen("Logado").ids.ContaEdit.switch_tab("EditarConta")
            except:
                pass
        else:
            pass

    def Pagamentos(self):
        if self.Connected == False:
            print("Deslogado")
        else:
            self.Cep = self.root.get_screen("ConfirmarCompra").ids.Cep.text
            self.NumeroResidencia1 = self.root.get_screen("ConfirmarCompra").ids.NumeroResidencia.text
            d = {
                'first_name': f'{self.NomeCompleto}',
                'cpf': f'{self.Cpf}',
                'cep': f'{self.Cep}',
                'NumeroResidencia': f'{self.NumeroResidencia}',
                'items': [],
            }
            for QuantidadeEscolhida in Carrinho.keys():
                print("Sku:", QuantidadeEscolhida)
                print(f"{Carrinho[QuantidadeEscolhida]}")
                d['items'].append({f'{QuantidadeEscolhida}': Carrinho[QuantidadeEscolhida]})
                print(d)
            SendMsg = "Pedidos:" + str(d)
            client.sendall(bytes(SendMsg, 'UTF-8'))
            in_data = client.recv(1024)
            webbrowser.open(in_data.decode())
if __name__ == "__main__":
    Loader.loading_image = 'loading.gif'

    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context
    MainApp().run()
