import os
   
def exibir_titulo():
    print("""
░░░░░██╗███╗░░░███╗  ██╗░░░██╗██╗██████╗░██████╗░░█████╗░░█████╗░░█████╗░██████╗░██╗░█████╗░
░░░░░██║████╗░████║  ██║░░░██║██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗
░░░░░██║██╔████╔██║  ╚██╗░██╔╝██║██║░░██║██████╔╝███████║██║░░╚═╝███████║██████╔╝██║███████║
██╗░░██║██║╚██╔╝██║  ░╚████╔╝░██║██║░░██║██╔══██╗██╔══██║██║░░██╗██╔══██║██╔══██╗██║██╔══██║
╚█████╔╝██║░╚═╝░██║  ░░╚██╔╝░░██║██████╔╝██║░░██║██║░░██║╚█████╔╝██║░░██║██║░░██║██║██║░░██║
░╚════╝░╚═╝░░░░░╚═╝  ░░░╚═╝░░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝\n""")


def exibir_opcao():
    print('1. Cadastrar peça')
    print('2. Listar lista')
    print('3. comprar peças')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print("Finalizando programa")

def opcao_invalida():
    print("Opçao Invalida")
    input("Aperte um botão para retornar")
    main()

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção:'))
    try:
        if opcao_escolhida == 1:
            print('Cadastrar peças')
        elif opcao_escolhida == 2:
            print('Listar peças')
        elif opcao_escolhida == 3:
            print('comprar peças')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_titulo()
    exibir_opcao()
    escolher_opcao()

if __name__ == "__main__":
    main()

