import random
from trabalho import Menu

dictCadastroDeUsuario: dict = {}
listaSenhaAleatoria: list = ["tre12", "papa34", "macadoamo4", "peixefeio"]
listaDeNovasSenhas: list = ["fres2", "prato34", "quiqui66", "hyuga676"]


def CadastroUsuarios():
    
    while True:
    
        novoUsuario = str(input("Informe um nome de usuario: "))
        senhaUsuario = random.choice(listaSenhaAleatoria)

        if novoUsuario in dictCadastroDeUsuario:
            
            print("Este nome de usuario ja consta em nosso sistema tente outro nome\n")
            print("Redirecionando a página de cadastro...\n")
        
        else:
        
            dictCadastroDeUsuario[novoUsuario] = senhaUsuario
            listaSenhaAleatoria.remove(senhaUsuario)
            print("Usuario Cadastrado com sucesso.")
            break

def RemoverUsuarios():
    
    remover = str(input("Informe o usuario a ser removido: "))

    if remover not in dictCadastroDeUsuario:

        print("Usuario Inexistente, não foi possivel remover")
        print("Redirecionando a página inicial...")
    
    else:
        
        del dictCadastroDeUsuario[remover]
        
        novasSenhas = random.choice(listaDeNovasSenhas)
        listaSenhaAleatoria.append(novasSenhas)
        print("Cadastro deletado do sistema.")
        

def Logar():

    contador: int = 3
    while contador >= 0:

        usuario = str(input("Informe o nome de usuario: "))
        senha = str(input("Informe a senha cadastrada: "))

        if (usuario, senha) in dictCadastroDeUsuario.items():

            print("Login realizado !")
            Menu()
            break
            
        
        elif (usuario, senha) not in dictCadastroDeUsuario.items() and contador > 0:
            
            print("Usuario ou senha incorretos")
            print("Tente novamente")
        
        else:
            
            print("Tentativas excedidas")
            print("Redirecionando a página inicial...")
    
        contador = contador - 1


def VerUsuariosCadastrados():

    print(dictCadastroDeUsuario)


def MenuLogin():
    
    print("--- SISTEMA DE LOGIN ---")

    while True:

        opcao = str(input('''Selecione uma opção\n
                            A - Cadastrar Usuario\n
                            B - Ver Usuarios\n
                            C - Remover usuario\n
                            D - Logar\n
                            X - Sair\n
                            --> ''')).upper()
        
        match opcao:

            case "A":
                
                CadastroUsuarios()
            
            case "B":
                
                VerUsuariosCadastrados()
            
            case "C":
                
                RemoverUsuarios()
            
            case "D":
                
                Logar()
                

            case "X":
                
                print("ENCERRANDO...")
                break

            case _:

                print("Opção Inválida.")
                

MenuLogin()

