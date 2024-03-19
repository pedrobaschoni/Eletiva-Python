from modelocliente import *
from modelovenda import *
from modeloproduto import *
from modeloitenvenda import *
from modeloController import *


def cadastrar():
    opt = 0

    while opt != 1 and opt != 2 and opt != 3:
        opt = int(input('- - - - - - Cadastro.\n1 - Cliente.\n2 - Produto.\n3 - Venda.\n'))

    if opt == 1:
        cliente = Cliente()
        cliente.lerDados()
        sql = cliente.insereDados()
        controleDAO.incluir(sql)
    elif opt == 2:
        produto = Produto()
        produto.lerDados()
        sql = produto.insereDados()
        controleDAO.incluir(sql)
    else:
        venda = Venda()
        venda.lerDados()
        sql = venda.insereDados()
        controleDAO.incluir(sql)
        for i in venda.itensvenda:
            sql = i.insereDados()
            controleDAO.incluir(sql)


def procurar():
    opt = 0
    id = 0
    opcao = ""

    while opt != 1 and opt != 2:
        opt = int(input('- - - - - - Procurar.\n1 - Aluno.\n2 - Produto.\n'))
        if opt == 1:
            opcao = "Aluno"
        else:
            opcao = "Produto"

    while id <= 0:
        id = int(input('Digite o código do {}:\n'.format(opcao)))

    if opt == 1:
        aluno = controleDAO.procura_registro(1, id)
        return aluno
    else:
        produto = controleDAO.procura_registro(2, id)
        return produto

def listar_produtos():
    controller = Controller()
    produtos = controller.listarProdutos()
    print("Produtos:")
    for produto in produtos:
        print("ID:", produto[0])
        print("Nome:", produto[1])
        print("Preço:", produto[3])
        print("Quantidade:", produto[2])
        print()
def listar_clientes():
    controller = Controller()
    clientes = controller.listarClientes()
    print("Clientes:")
    for cliente in clientes:
        print("ID:", cliente[0])
        print("Nome:", cliente[1])
        print("Endereço:", cliente[2])
        print("Telefone:", cliente[3])
        print("Cidade:", cliente[4])
        print("UF:", cliente[5])
        print("CEP:", cliente[6])
        print()

def listar_vendas():
    controller = Controller()
    vendas = controller.listarVendas()
    print("Vendas:")
    for venda in vendas:
        print("ID:", venda[0])
        print("ID Cliente:", venda[1])
        print("Valor Total:", venda[2])
        print("Data:", venda[3])
        print()


def listar():
    print("1. Listar Produtos")
    print("2. Listar Clientes")
    print("3. Listar Vendas")
    print("4. Listar Todos")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_produtos()
    elif opcao == "2":
        listar_clientes()
    elif opcao == "3":
        listar_vendas()
    elif opcao == "4":
        listar_produtos()
        listar_clientes()
        listar_vendas()
    else:
        print("Opção inválida!")


def menu():
    while True:
        print('1 - Cadastrar')
        print('2 - Listar')
        print('3 - Sair\n\n')

        opt = int(input(''))

        match opt:
            case 1:
                cadastrar()
            case 2:
                listar()
            case 3:
                break
        print()

if __name__ == "__main__":

    cliente = Cliente()
    produto = Produto()
    venda = Venda()
    controleDAO = Controller()

    controleDAO.ob.configura(ho='localhost', db='trabalho', us='root', se='ifsp')

    menu()
