import random

class Jogos_Geral:

    def __init__(self):
        self.dados = ''

    def gera_jogo(self, qtde, maximo, tamanho):
        retorno = []
        for i in range(qtde):
            cartela = []
            while True:
                dezena = random.Random().randint(1, maximo)
                if not dezena in cartela:
                    cartela.append(dezena)
                if len(cartela) == tamanho:
                    break
            cartela = [str(x+100)[1:3] for x in cartela]
            cartela.sort()
            retorno.append(" ".join(cartela))
        return retorno

    def confere(self, entrada, numero):
        retorno = []
        for i in entrada:
            if numero in i:
                retorno.append(i)
        return retorno

    def remove(self, entrada, acima):
        retorno = []
        for x in entrada:
            x = x.split()
            x = [i if i >= acima else "--" for i in x]
            retorno.append(" ".join(x))
        return retorno

