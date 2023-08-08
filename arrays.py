# Cria uma array com o número de elementos definidos pelo usuário
nomes = []
itens = eval(input("Defina o número de itens na lista: "))

i = 0
while i < itens:
    nomes.append(input("Informe um nome a adicionar: "))
    i += 1

print(f"Exemplo 1: Array criada com o número de elementos definido pelo usuário: {nomes}\n")

numeros = []
itens = 10
i = 1

# Preenche uma array com incrementos de 1 até o limite de itens
while i <= itens:
    numeros.append(i)
    i += 1

print(f"Exemplo 2: A array com a ordem original dos elementos é {numeros}\n")

# Inverte a ordem do conteúdo de uma array
listaInvertida = []
i = len(numeros)
while i > 0:
    listaInvertida.append(i)
    i -= 1

print(f"Exemplo 3: O resultado da inversão da ordem da array é {listaInvertida}\n")


# Soma o conteúdo de cada índice das arrays gerando uma nova array
listaSoma = []
tamanhoDaLista = len(numeros)


menu = eval(input("Exemplo 4: Informe a operação desejada 1: Soma, 2: Subtração, 3: Divisão ou 4: Multiplicação"))
if menu == 1:
    for i in range(tamanhoDaLista):
        listaSoma.append(numeros[i] + listaInvertida[i])
        i += 1
    print(f"O resultado da soma do conteúdo de cada índice da array é {listaSoma}\n")

elif menu == 2:
    for i in range(tamanhoDaLista):
        listaSoma.append(numeros[i] - listaInvertida[i])
        i += 1
    print(f"O resultado da subtração do conteúdo de cada índice da array é {listaSoma}\n")

elif menu == 3:
    for i in range(tamanhoDaLista):
        listaSoma.append(numeros[i] / listaInvertida[i])
        i += 1
    print(f"O resultado da divisão do conteúdo de cada índice da array é {listaSoma}\n")

else:
    for i in range(tamanhoDaLista):
        listaSoma.append(numeros[i] * listaInvertida[i])
        i += 1
    print(f"O resultado da multiplicação do conteúdo de cada índice da array é {listaSoma}\n")

# Realizando pesquisas no conteúdo de uma array
# A variável PESQUISA receberá o termo pesquisado na array,
# RESULTADO mudará para True caso o item seja encontrado
# P é a variável utilizada para o incremento e referência ao índice na array

pesquisa = eval(input("Exemplo 5: Informe o item que deseja procurar na lista original: "))
resultado = False
p = 0

# Para P no RANGE representado pelo TAMANHO DA ARRAY
for p in range(len(numeros)):
    if pesquisa == numeros[p]:
        resultado = True
        break
    else:
        p += 1

if resultado == True:
    print(f"O valor {pesquisa} foi encontrado e ocupa o índice {p} na array!")
else:
    print(f"A array não contém o item {pesquisa}.")
