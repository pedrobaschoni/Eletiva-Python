from jogos import Jogos_Geral

jogo = Jogos_Geral()

lista = jogo.gera_jogo(5, 60, 8)
primeiralista = lista
for i in lista:
    print(i)

lista = jogo.confere(lista, '10')
if len(lista)>0:
    print('\nConferencia')
    for i in lista:
        print(i)

lista = jogo.remove(primeiralista, '15')
print('\nRemovidos acima')
for i in lista:
    print(i)