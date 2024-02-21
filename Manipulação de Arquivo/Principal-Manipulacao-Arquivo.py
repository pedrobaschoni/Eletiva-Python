with open('Q:/arquivoex/dados.txt', 'r') as arquivos: #Coloque o caminho para o arquivo baixado do github
    dados = arquivos.read().split('\n')

procurado = input("Digite a sequencia procurada: ")
somatoria = {x:0 for x in range(0,7)}
for i in dados:
    i = i.split()[2:]
    numeros = i
    #i = [int (x) for x in i]
    i = ['1' if int(x) % 2 == 0 else '0' for x in i]
    soma = sum([int(x) for x in i])

    somatoria[soma]+=1
    if "".join(i) == procurado:
        print(procurado, " ".join(numeros))

somatoria = dict(sorted(somatoria.items()))
for k in somatoria:
    print(k, '->', somatoria[k])