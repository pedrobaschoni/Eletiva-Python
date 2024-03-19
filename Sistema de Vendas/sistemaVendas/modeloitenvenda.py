from modeloController import *

class Itenvenda:

    def __init__(self):
        self.__idproduto = ''
        self.__idvenda = ''
        self.__qtde = ''
        self.__valor = ''

    @property
    def idproduto(self):
        return self.__idproduto

    @idproduto.setter
    def idproduto(self, idproduto):
        self.__idproduto = idproduto

    @property
    def idvenda(self):
        return self.__idvenda

    @idvenda.setter
    def idvenda(self, idvenda):
        self.__idvenda = idvenda

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
        self.__sql = "insert into itenvenda (idvenda, idproduto, qtde, valor) values"
        self.__sql += ("('{}','{}','{}','{}')".format(self.idvenda,
                                                      self.idproduto,
                                                      self.qtde,
                                                      self.valor))
        return self.__sql

    def lerDados(self, idvenda):
        self.__idvenda = idvenda
        self.__idproduto = int(input("Digite o ID do produto: "))
        self.__qtde = input("Digite a quantidade do produto: ")
        controleDAO = modeloController.Controller()
        controleDAO.ob.configura(ho='localhost', db='trabalho', us='root', se='ifsp')
        preco = controleDAO.precoProduto(self.__idproduto)
        self.__valor = preco * float(self.__qtde)

