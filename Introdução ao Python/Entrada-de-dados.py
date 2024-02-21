#ENTRADA DE DADOS NO PYTHON

nome = input("Nome: ");
idade1 = input("Idade: ");
idade2 = int(input("Idade: "));
valor = input("Valor: ")


print("Antes da conversao ==========================")
print(type(nome))
print(type(idade1))
print(type(idade2))
print(type(valor))

print("Depois da conversao =========================")
if idade1.isnumeric():
   idade3 = int(idade1)
   print("convertido")


#ENTRADA DE DADOS UTILIZANDO BIBLITOECA PROMPT
import prompt

numero = prompt.integer(prompt="Entre com um numero: ")
email = prompt.email("Seu e-mail:")
nome = prompt.string("Seu nome: ")

#SAIDA DE DADOS NA TELA
nome = "Pedro"
cidade = "Epitacio"

print(f'Ola {nome}, bem vindo ao curso em {cidade}')
print("%s Bem vindo %s"%("Pedro","Epitacio"))
print("Olá, {} e {}!".format('pessoa1','pessoa2'))

print('{:,}'.format(1234567890))
print('Gasolina: R${:.2f}'.format(4.356))
print('Respostas corretas: {:.2%}'.format(53/60))


#MANIPULAÇÃO DE STRING
nome = 'pedro baschoni'
print(nome[0:nome.index(" ")].title())      # Pedro
print(nome[0:nome.find(("s"))])             # ped
print(nome[0:3])                            # ped
print(nome[7:14].upper())                   # BASCHONI
print(nome.split())                         # ['pedro','baschoni']
print(nome.replace("lucas","baschoni"))  # pedro baschoni
letrasnome = [x for x in nome[:6]]
print(letrasnome)                           # ['p','e','d','r','o']
print(nome[6:])                             # baschoni
print(nome[::-1])                           # inohcsab ordep
print(" lucas ".join(nome.split(" ")))  # pedro lucas baschoni

#COMANDO REPETIÇÃO FOR
nome = ["PEDRO","ABIGAIL"]

for key, value in enumerate(nome):
    print (key, value)
print("-------------------------")

for key in nome[0]:
    print(key*(nome[0].index(key)+1))
else:
    print("---------------------")

for i in ['Tamanduá', 'Tatu', 'Boto Cor-De-Rosa']:
    print(i)

for i in range(10):
    print(i)

for i in range(5,10,2):
    print(i)

k = [('a','b1','c1','d1','e1')]
for a,b,c,d,e in k:
    print(a,b,c,d,e)
