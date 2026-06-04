listaLivros: list = []

def CadastrarLivros():

    cadastrarLivros = str(input("Informe o nome do livro a ser cadastrado: ")).upper()
    

    if cadastrarLivros in listaLivros:

        print("Livro já cadastrado")
        print("Redirecionando ao menu Inicial...\n")
    
    else:
        
        listaLivros.append(cadastrarLivros)
        
        print("\nCadastro Realizado Com Sucesso.\n")
        print("Redirecionando ao menu Inicial...\n")


def VerLivrosCadastrados():

    listaLivros.sort()
    for livros in listaLivros:
        print(livros)

    # se a minha lista de livros estiver vazia eu aviso ao usuario que a lista esta vazia e encaminho o usuario ao menu inicial ou a pagina de cadastro de livos

def RemoverLivros():

    remover = str(input("Informe o livro que deseja remover: ")).upper()
    

    if remover not in listaLivros:

        print("Nome incorreto impossivel remover o livro")
        print("Redirecionando a Página Inicial...\n")
    
    else:

        listaLivros.remove(remover)
        
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




