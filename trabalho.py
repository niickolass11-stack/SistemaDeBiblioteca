# Criar Um sistema de biblioteca 
# cadastrar livros
# Listar Livros
# Sair

listaLivros: list = []

def CadastrarLivros():

    cadastrarLivros = str(input("Informe o nome do livro a ser cadastrado: ")).upper()
    listaLivros.append(cadastrarLivros)

    # Se o meu livro cadastrado ja exixtir dentro da minha lista eu aviso ao usuario que o livro ja existe

    print("\nCadastro Realizado Com Sucesso.\n")
    print("Redirecionando ao menu Inicial...\n")

def VerLivrosCadastrados():

    listaLivros.sort()
    print(listaLivros)

    # se a minha lista de livros estiver vazia eu aviso ao usuario que a lista esta vazia e encaminho o usuario ao menu inicial ou a pagina de cadastro de livos

def RemoverLivros():

    remover = str(input("Informe o livro que deseja remover: ")).upper()
    listaLivros.remove(remover)
    
    # se o usuario digitar o nome errado eu dou uma mensagem ao usuario dizendo que este livro nao existe e dou a lista dos livros existentes para ele 
    print("\nLivro Removido Com Sucesso.\n")
    print("Redirecionando a Página Inicial...\n")


def Menu():

    print("--- BEM VINDO A BIBLIOTECA DIGITAL --- ")

    while True:

        opcao = str(input('''Selecione uma das opções\n
                            A - Cadastrar Livros\n
                            B - Remover Livros\n
                            C - Ver Lista de Livros\n
                            X - Sair\n
                            --> ''')).upper()

        match opcao:

            case "A":

                CadastrarLivros()
                
                
            case "B":

                RemoverLivros()
                
            case "C":

                VerLivrosCadastrados()
                
                
            case "X":

                print("Encerrando...")
                break
                    
            case _:
                
                print("Opção Inválida")

Menu()