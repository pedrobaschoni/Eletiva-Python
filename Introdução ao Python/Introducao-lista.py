lista =[]
lista = [10,30,40,50,60,70]

lista.append(31)
lista.append(32)

print(lista)
lista.remove(50)

print(lista)
lista.sort()
print(lista,"ordenada")
lista.sort(reverse=True)
print(lista,"ordem inversa")

lista.append("Joao")
lista.append([3,5,6])
print(lista)

print(lista.extend(['joia','goiaba']))

l = ['O', 'r', 'd', 'e', 'm', ' ', 'e', ' ', 'P', 'r', 'o', 'g', 'r', 'e', 's', 's', 'o']
print(''.join(l))

for i in lista:
    if type(i)==list:
       print(sum(i))
       print(max(i))

for i,valor in enumerate(lista):
    print("Indice {} valor {}".format(i,valor))