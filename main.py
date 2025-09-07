from app.animais import inserir_animal, listar_animais, atualizar_animal, deletar_animal

def exibir_menu():
    """Exibe o menu principal de opções para o usuário."""
    print("\n===== SISTEMA DE CADASTRO DE ANIMAIS DE ESTIMAÇÃO =====")
    print("1 - Inserir novo animal")
    print("2 - Listar todos os animais")
    print("3 - Atualizar dados de um animal")
    print("4 - Deletar animal")
    print("0 - Sair")

def main():
    """Função principal que controla o fluxo do programa."""
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_animal()
        elif opcao == "2":
            listar_animais()
        elif opcao == "3":
            atualizar_animal()
        elif opcao == "4":
            deletar_animal()
        elif opcao == "0":
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
