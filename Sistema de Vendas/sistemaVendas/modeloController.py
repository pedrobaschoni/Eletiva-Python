from conectarbanco import *
from modelocliente import *
from modelovenda import *
from modeloproduto import *


class Controller:

    def __init__(self):
        self.ob = Banco()
        self.ob.configura(ho="localhost", db="trabalho", us="root", se="ifsp")

    def incluir(self, sqlParam):
        self.ob.abrirConexao()

        sql = sqlParam

        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except:
            print("Houve um erro")
            print(sqlParam)
            self.ob.descarte()

    def procura_registro(self, opcao, id):
        self.ob.abrirConexao()

        if opcao == 1:
            sql = ("select * from aluno where id = '{}'".format(id))
            aluno = self.ob.selectQuery(sql)

            retorno = Aluno()
            if len(aluno) >= 1:
                retorno.setAluno(aluno[0][0],
                                 aluno[0][1],
                                 aluno[0][2],
                                 aluno[0][3],
                                 aluno[0][4],
                                 aluno[0][5],
                                 aluno[0][6],
                                 aluno[0][7])
            return retorno
        else:
            sql = ("select * from produto where id = '{}'".format(id))
            produto = self.ob.selectQuery(sql)
            retorno = Produto()
            if len(produto) >= 1:
                retorno.setProduto(produto[0][0],
                                   produto[0][1],
                                   produto[0][2],
                                   produto[0][3])
            return retorno

    def listaTodos(self, opcao):
        retorno = []

        self.ob.abrirConexao()

        if opcao == 1:
            retorno = self.ob.selectQuery("select * from aluno")
            alunos = []
            for item in retorno:
                aluno = Aluno()
                aluno.setAluno(*item)
                alunos.append(aluno)
            return alunos
        else:
            retorno = self.ob.selectQuery("select * from produto")
            produtos = []
            for item in retorno:
                produto = Produto()
                produto.setProduto(*item)
                produtos.append(produto)
            return produtos

    def precoProduto(self, idproduto):
        self.ob.abrirConexao()

        # Consulta SQL para obter o preço do produto com base no ID
        sql = ("SELECT preco FROM produto WHERE idproduto = '{}'".format(idproduto))
        resultado = self.ob.selectQuery(sql)

        if resultado:
            # Retorne o preço do produto
            return resultado[0][0]
        else:
            print("Produto não encontrado.")
            return None

    def ultimoIdVenda(self):
        self.ob.abrirConexao()

        # Consulta SQL para obter o último ID de venda inserido
        sql = "SELECT MAX(idvenda) FROM venda"
        resultado = self.ob.selectQuery(sql)

        if resultado:
            # Retorne o último ID de venda
            return resultado[0][0]
        else:
            print("Nenhuma venda encontrada.")
            return 1

    def executar(self, sql):
        self.ob.abrirConexao()
        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except Exception as e:
            print("Houve um erro:", e)
            print(sql)
            self.ob.descarte()

    def listarClientes(self):
        clientes = []
        self.ob.abrirConexao()
        resultado = self.ob.selectQuery("SELECT * FROM cliente")
        for item in resultado:
            cliente = item
            clientes.append(cliente)
        return clientes

    def listarVendas(self):
        vendas = []
        self.ob.abrirConexao()
        resultado = self.ob.selectQuery("SELECT * FROM venda")
        for item in resultado:
            venda = item
            vendas.append(venda)
        return vendas

    def listarProdutos(self):
        produtos = []
        self.ob.abrirConexao()
        sql = "SELECT * FROM produto"
        resultado = self.ob.selectQuery(sql)
        for item in resultado:
            produto = item
            produtos.append(produto)
        return produtos

    def consultar(self, sql):
        self.ob.abrirConexao()
        try:
            resultado = self.ob.selectQuery(sql)
            return resultado
        except Exception as e:
            print("Houve um erro:", e)
            print(sql)

        produtos = []
        self.ob.abrirConexao()
        resultado = self.ob.selectQuery("SELECT * FROM produto")
        for item in resultado:
            produto = Produto()
            produto.setProduto(*item)
            produtos.append(produto)
        return produtos