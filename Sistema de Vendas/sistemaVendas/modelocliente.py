
class Cliente:

    def __init__(self):
        self.__idcliente = ''
        self.__nome = ''
        self.__endereco = ''
        self.__telefone = ''
        self.__cidade = ''
        self.__uf = ''
        self.__cep = ''

    @property
    def idcliente(self):
        return self.__idcliente

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def telefone(self):
        return self.__telefone

    @property
    def cidade(self):
        return self.__cidade

    @property
    def uf(self):
        return self.__uf

    @property
    def cep(self):
        return self.__cep

    @nome.setter
    def nome(self, entrada):
        self.__nome = entrada

    @endereco.setter
    def endereco(self, entrada):
        self.__endereco = entrada

    @telefone.setter
    def telefone(self, entrada):
        self.__telefone = entrada

    @cidade.setter
    def cidade(self, entrada):
        self.__cidade = entrada

    @uf.setter
    def uf(self, entrada):
        self.__uf = entrada

    @cep.setter
    def cep(self, entrada):
        self.__cep = entrada

    def insereDados(self):
        self.__sql = "insert into cliente (nome, endereco, telefone, cidade, uf, cep) values"
        self.__sql += ("('{}','{}','{}','{}','{}','{}')".format(self.nome,
                                                                          self.endereco,
                                                                          self.telefone,
                                                                          self.cidade,
                                                                          self.uf,
                                                                          self.cep))
        return self.__sql

    def lerDados(self):
        self.__nome = input("Digite o nome do cliente: ")
        self.__endereco = input("Digite o endereço do cliente: ")
        self.__telefone = input("Digite o telefone do cliente: ")
        self.__cidade = input("Digite a cidade do cliente: ")
        self.__uf = input("Digite o UF do cliente: ")
        self.__cep = input("Digite o CEP do cliente: ")
