class Manipulador_de_Strings:
    def __init__(self, entrada):
        self.texto = entrada

    def inverterTexto(self):
       return self.texto[::-1]

    def maiuscula(self):
        return self.texto.upper()

    def setTexto(self, texto):
        self.texto = texto

    def abreviar(self):
        x = self.texto.split()
        primeiro = x[0]
        ultimo = x[len(x)-1]
        for i in range(1,len(x)-1): # 1... ate o fim do vetor
            if not x[i] in 'DE, DOS, DA':
                x[i] = x[i][0]+'.'

        return " ".join(x)
