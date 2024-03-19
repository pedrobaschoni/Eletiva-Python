import modeloController
from modeloController import *

class Produto:

    def __init__(self):
        self.__idproduto = ''
        self.__nome = ''
        self.__qtde = ''
        self.__valor = ''

    @property
    def idproduto(self):
        return self.__idproduto

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def qtde(self):
        return self.__qtde

    @qtde.setter
    def qtde(self, qtde):
        self.__qtde = qtde

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    def insereDados(self):
        self.__sql = "insert into produto (nome, qtde, preco) values"
        self.__sql += ("('{}','{}','{}')".format(
            self.nome,
            self.qtde,
            self.valor))
        return self.__sql

    def lerDados(self):
        self.__nome = input("Digite o nome do produto: ")
        self.__qtde = input("Digite a quantidade do produto: ")
        self.__valor = input("Digite o valor do produto: ")

    def verificarEstoque(self, idproduto, quantidade):
        controleDAO = modeloController.Controller()
        controleDAO.ob.configura(ho='localhost', db='trabalho', us='root', se='ifsp')
        quantidade_estoque = controleDAO.consultar(f'SELECT qtde FROM produto WHERE idproduto = {idproduto}')
        if quantidade_estoque:
            quantidade_estoque = quantidade_estoque[0][0]
            if int(quantidade) <= int(quantidade_estoque):
                return True
        print("Não há estoque suficiente para o produto com ID:", idproduto)
        return False

    def atualizarEstoque(self, idproduto, quantidade):
        controleDAO = modeloController.Controller()
        controleDAO.ob.configura(ho='localhost', db='trabalho', us='root', se='ifsp')
        controleDAO.executar(f'UPDATE produto SET qtde = qtde - {quantidade} WHERE idproduto = {idproduto}')

