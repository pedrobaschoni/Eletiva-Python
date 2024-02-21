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
nome = "Vilson"
cidade = "Epitacio"

print(f'Ola {nome}, bem vindo ao curso em {cidade}')
print("%s Bem vindo %s"%("Vilson","Epitacio"))
print("Olá, {} e {}!".format('pessoa1','pessoa2'))

print('{:,}'.format(1234567890))
print('Gasolina: R${:.2f}'.format(4.356))
print('Respostas corretas: {:.2%}'.format(53/60))


#MANIPULAÇÃO DE STRING
nome = 'vilson maziero'
print(nome[0:nome.index(" ")].title())      # Vilson
print(nome[0:nome.find(("s"))])             # vil
print(nome[0:3])                            # vil
print(nome[7:14].upper())                   # MAZIERO
print(nome.split())                         # ['vilson','maziero']
print(nome.replace("maziero","francisco"))  # vilson francisco
letrasnome = [x for x in nome[:6]]
print(letrasnome)                           # ['v','i','l','s','o','n']
print(nome[7:])                             # maziero
print(nome[::-1])                           # oreizam nosliv
print(nome[::2])                            # vls air
print(" francisco ".join(nome.split(" ")))  # vilson francisco maziero

#COMANDO REPETIÇÃO FOR
nome = ["VILSON","JOAO"]

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