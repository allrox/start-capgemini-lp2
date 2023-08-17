from random import randrange

# Definindo uma lista para teste
lista = []


def elementos_aleatorios(y):
    for x in range(y):
        # Adiciona à lista um número aleatório na faixa entre 'start' e 'stop'
        lista.append(randrange(0, 5000))


elementos_aleatorios(30)
print(f"Lista com os elementos na ordem original {lista}")

# Captura o tamanho da lista
n = len(lista)

# Laço de comparação
for i in range(n):

    # Para cada índice no range de 0 a n-i-1 Desta forma, a cada passagem o loop interno
    # reduz o número de comparações desnecessárias, já que o maior elemento SEMPRE flutua
    # para o final da lista na primeira passagem. Assim, na repetições do laço principal
    # pode-se subtrair um elemento sem prejuízo da função
    for j in range(0, n-i-1):
        # Se o item do índice J for maior que o elemento do próximo índice
        if lista[j] > lista[j+1]:
            # Os elementos trocam de posição em seus índices
            lista[j], lista[j+1] = lista[j+1], lista[j]


print(f"Lista com elementos reordenados {lista}")
print(f"Foram ordenados {n} elementos.")
