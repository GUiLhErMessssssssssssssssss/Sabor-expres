import os

pecas = [{'nome': 'Paça', 'categoria': 'vidro temperado', 'ativo': False},
         {'nome': 'peça', 'categoria': 'janela', 'ativo': True},
         {'nome': 'peça', 'categoria': 'box', 'ativo': False}]

def exibir_nome_do_programa():
    """Essa função é responsável por exibir o nome da aplicação"""
    print("""

░░░░░██╗███╗░░░███╗  ██╗░░░██╗██╗██████╗░██████╗░░█████╗░░█████╗░░█████╗░██████╗░██╗░█████╗░
░░░░░██║████╗░████║  ██║░░░██║██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗
░░░░░██║██╔████╔██║  ╚██╗░██╔╝██║██║░░██║██████╔╝███████║██║░░╚═╝███████║██████╔╝██║███████║
██╗░░██║██║╚██╔╝██║  ░╚████╔╝░██║██║░░██║██╔══██╗██╔══██║██║░░██╗██╔══██║██╔══██╗██║██╔══██║
╚█████╔╝██║░╚═╝░██║  ░░╚██╔╝░░██║██████╔╝██║░░██║██║░░██║╚█████╔╝██║░░██║██║░░██║██║██║░░██║
░╚════╝░╚═╝░░░░░╚═╝  ░░░╚═╝░░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝""")

def exibir_opcoes():
    """Essa função é responsável por exibir os menus"""
    print("1. Cadastrar peças")
    print("2. Listar peças")
    print("3. Apagar peça")
    print("4. Sair\n")

def finalizar_app():
    """Essa função é responsável por encerrar o aplicativo"""
    exibir_subtitulo("Finalizar app")
    print("Aplicativo encerrado.")
    exit()

def voltar_ao_menu_principal():
    """Essa função é responsável por voltar à tela principal após teclar qualquer caractere + Enter"""
    input("\nDigite uma tecla para voltar ao menu principal: ")
    main()

def opcao_invalida():
    """Essa função é responsável por sinalizar ao usuário que a opção escolhida é inválida e retornar à tela principal"""
    print("Opção inválida\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    """Essa função cria um padrão de exibição para os títulos do menu escolhido"""
    os.system('clear' if os.name == 'nt' else 'clear')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_nova_peca():
    """Essa função é responsável por cadastrar uma nova peça"""
    exibir_subtitulo("Cadastro de novas peças")
    nome_da_peca = input("Digite o nome da peça que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria da peça {nome_da_peca}: ")
    dados_da_peca = {'nome': nome_da_peca, 'categoria': categoria, 'ativo': False}
    pecas.append(dados_da_peca)
    print(f"A peça {nome_da_peca} foi cadastrada com sucesso!")
    voltar_ao_menu_principal()

def listar_pecas():
    """Essa função é responsável por listar as peças cadastradas"""
    exibir_subtitulo("Lista de peças")
    print(f"{'Nome da peça'.ljust(23)} | {'Categoria'.ljust(20)} | {'Status'}")
    for peca in pecas:
        nome_peca = peca['nome']
        categoria = peca['categoria']
        ativo = "ativado" if peca['ativo'] else "desativado"
        print(f" - {nome_peca.ljust(20)} | {categoria.ljust(20)} | {ativo}")
    voltar_ao_menu_principal()

def alterar_estado_peca():
    """Essa função é responsável por alterar o estado/status da peça (ativado/desativado)"""
    exibir_subtitulo('Alterando estado da peça')
    nome_peca = input("Digite o nome da peça que deseja alterar o estado: ")
    peca_encontrada = False

    for peca in pecas:
        if nome_peca.lower() == peca['nome'].lower():
            peca_encontrada = True
            peca['ativo'] = not peca['ativo']
            mensagem = f"A peça {nome_peca} foi ativada com sucesso" if peca['ativo'] else f"A peça {nome_peca} foi desativada com sucesso"
            print(mensagem)

    if not peca_encontrada:
        print("A peça não foi encontrada.")

    voltar_ao_menu_principal()

def escolher_opcao():
    """Essa função é responsável por permitir a seleção do menu"""
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        print(f"Você escolheu a opção {opcao_escolhida}")

        if opcao_escolhida == 1:
            cadastrar_nova_peca()
        elif opcao_escolhida == 2:
            listar_pecas()
        elif opcao_escolhida == 3:
            alterar_estado_peca()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    """Essa função reseta o programa para a tela principal, exibindo o nome e os menus"""
    os.system('clear' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()