from modeloController import *
from modeloitenvenda import *
from modeloproduto import *

class Venda:

    def __init__(self):
        self.__idcliente = ''
        self.__idvenda = ''
        self.__valortotal = ''
        self.__data = ''
        self.__itensvenda = []

    @property
    def idcliente(self):
        return self.__idcliente

    @property
    def idvenda(self):
        return self.__idvenda

    @property
    def valortotal(self):
        return self.__valortotal

    @property
    def data(self):
        return self.__data

    @idcliente.setter
    def idcliente(self, entrada):
        self.__idcliente = entrada

    @idvenda.setter
    def idvenda(self, entrada):
        self.__idvenda = entrada

    @valortotal.setter
    def valortotal(self, entrada):
        self.__valortotal = entrada

    @data.setter
    def data(self, entrada):
        self.__data = entrada

    @property
    def itensvenda(self):
        return self.__itensvenda

    @itensvenda.setter
    def itensvenda(self, itensvenda):
        self.__itensvenda = itensvenda

    def insereDados(self):
        self.__sql = "insert into venda (idcliente, valortotal, data) values"
        self.__sql += ("('{}','{}','{}')".format(
                                                      self.idcliente,
                                                      self.valortotal,
                                                      self.data))
        for i in self.__itensvenda:
            i.insereDados()

        return self.__sql

    def lerDados(self):
        self.__data = input("Digite a data da venda (AAAA-MM-DD): ")
        self.__idcliente = input("Digite o ID do cliente: ")
        controleDAO = modeloController.Controller()
        controleDAO.ob.configura(ho='localhost', db='trabalho', us='root', se='ifsp')
        aux = controleDAO.ultimoIdVenda()
        if aux is None:
            aux = 0
        self.__idvenda = aux + 1
        self.lerItenVendas()

    def lerItenVendas(self):
        soma = 0
        produto = Produto()
        while True:
            itenvenda = Itenvenda()  # Criar um novo objeto a cada iteração
            itenvenda.lerDados(self.__idvenda)

            estoque_suficiente = produto.verificarEstoque(itenvenda.idproduto,itenvenda.qtde)
            if not estoque_suficiente:
                print("Não há estoque suficiente para este produto.")
                continue
            soma += itenvenda.valor
            self.__itensvenda.append(itenvenda)
            produto.atualizarEstoque(itenvenda.idproduto,itenvenda.qtde)  # Descontar do estoque
            if input('Deseja adicionar mais produtos? (S / N): ').upper() == 'N':
                break
        self.__valortotal = soma

