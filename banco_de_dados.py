clientes = ["Jorge", "João", "Maria", "André", "Ana", "Pedro", "Claudio", "Carla", "Daniel", "Priscilla",
            "Ricardo", "Joana", "Cristiane", "Cristina", "Paula", "Cláudia", "Carlos", "Bruno", "Eduardo"]


def listar_clientes(array):
    """
    Imprime uma Array
    :param array: Recebe a array que terá seu conteúdo impresso
    :return: str
    """
    if len(array) > 1:
        x = "elementos"
    else:
        x = "elemento"
    print(f"A array Clientes contém {len(array)} {x}.\n{array}\n")


def cadastrar():
    """
    Cadastra um novo cliente na array Clientes
    :return: str
    """
    clientes.append(input("Informe o nome para cadastro: "))
    print(f"Nome cadastrado no índice {len(clientes) - 1}\n")


def pesquisar():
    """
    Realiza a busca do conteúdo do input na array Clientes
    :return: str
    """
    busca = input("Informe o nome que deseja pesquisar: ")
    encontrado = False

    for i in range(len(clientes)):
        if busca == clientes[i]:
            print(f"Nome encontrado no índice {i} da lista de clientes.\n")
            encontrado = True
            break
        else:
            i += 1

    if not encontrado:
        print("Nome não localizado!\n")


def excluir(array):
    """
    Exclui o conteúdo de uma array pelo índice informado
    :param array:
    :return: str
    """
    try:
        busca = int(input("Informe o índice a ser excluído: "))
        if 0 <= busca < len(array):
            confirma = input(f"Tem certeza de que deseja excluir o item '{busca}'?\n"
                             f"Digite SIM para sim ou outro caractere para cancelar: \n")
            if confirma == "SIM":
                clientes.pop(busca)
                print(f"Nome excluído do índice {busca}.\n")
            else:
                print("Exclusão cancelada!")
        else:
            print("Índice inválido!")

    except ValueError:
        print("Erro: Desculpe, ocorreu um erro ao tentar excluir.")


def mostrar_menu():
    """
    Exibe o menu com opções da aplicação
    :return: str
    """
    # print("1: Cadastrar")
    # print("2: Pesquisar")
    # print("3: Excluir")
    # print("4: Listar Clientes")
    # print("5: Sair")

    try:
        escolha = int(input("[1]Cadastrar\n[2]Pesquisar\n[3]Excluir\n[4]Listar\n[5]Sair"))
        while escolha != 5:
            if escolha == 1:
                cadastrar()
            elif escolha == 2:
                pesquisar()
            elif escolha == 3:
                excluir(clientes)
            elif escolha == 4:
                listar_clientes(clientes)
            else:
                print("Escolha inválida")

            escolha = int(input("Escolha uma opção: "))

    except ValueError:
        print(f"***** Erro: Utilize um dos números apresentados no menu. *****\n")
        mostrar_menu()


mostrar_menu()
