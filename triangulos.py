# Entrada dos valores para os lados do objeto
print("Informe as medidas dos lados, A, B e C:")
a = int(input())
b = int(input())
c = int(input())


# Função para validar se o objeto é um triângulo
def valida_triangulo(a, b, c):
    if a > (b + c) or b > (c + a) or c > (a + b):
        return False
    else:
        return True


# Função para classificar o triângulo quanto às medidas dos lados
def classifica_triangulo(a, b, c):

    if valida_triangulo(a, b, c) == True:
        if a == b == c:
            print(f"Em relação aos lados {a}, {b} e {c}, é um triângulo equilátero.")
        elif a == b != c or b == c != a or c == a != b:
            print(f"Em relação aos lados {a}, {b} e {c}, é um triângulo isósceles.")
        else:
            print(f"Em relação aos lados {a}, {b} e {c}, é um triângulo escaleno.")
    else:
        print(f"O objeto com lados {a}, {b} e {c}, não é um triângulo.")


classifica_triangulo(a, b, c)
