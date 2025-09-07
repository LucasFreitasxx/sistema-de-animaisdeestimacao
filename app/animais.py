from app.db import conectar  # Importa a função que conecta ao banco MySQL

def inserir_animal():
    """Insere um novo animal de estimação no banco de dados."""
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        try:
            # Coleta os dados do animal
            nome = input("Nome do animal: ")
            especie = input("Espécie (ex: cão, gato): ")
            raca = input("Raça: ")
            idade = input("Idade: ")
            nome_dono = input("Nome do dono: ")

            comando = """
                INSERT INTO animais (nome, especie, raca, idade, nome_dono)
                VALUES (%s, %s, %s, %s, %s)
            """
            valores = (nome, especie, raca, idade, nome_dono)
            cursor.execute(comando, valores)
            conexao.commit()
            print("Animal inserido com sucesso!")
        except Exception as erro:
            print(f"Erro ao inserir animal: {erro}")
        finally:
            cursor.close()
            conexao.close()

def listar_animais():
    """Lista todos os animais cadastrados em ordem alfabética."""
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        try:
            cursor.execute("SELECT * FROM animais ORDER BY nome ASC")
            resultados = cursor.fetchall()

            print("\n--- Lista de Animais ---")
            for animal in resultados:
                print(f"ID: {animal[0]} | Nome: {animal[1]} | Espécie: {animal[2]} | Raça: {animal[3]} | Idade: {animal[4]} | Dono: {animal[5]}")
        except Exception as erro:
            print(f"Erro ao listar animais: {erro}")
        finally:
            cursor.close()
            conexao.close()

def atualizar_animal():
    """Atualiza os dados de um animal pelo ID informado."""
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        try:
            cursor.execute("SELECT * FROM animais ORDER BY id ASC")
            resultados = cursor.fetchall()

            print("\n--- Animais disponíveis para atualizar ---")
            for animal in resultados:
                print(f"ID: {animal[0]} | Nome: {animal[1]} | Espécie: {animal[2]}")

            id_animal = input("\nDigite o ID do animal que deseja atualizar: ")

            print("Informe os novos dados:")
            nome = input("Novo nome: ")
            especie = input("Nova espécie: ")
            raca = input("Nova raça: ")
            idade = input("Nova idade: ")
            nome_dono = input("Novo nome do dono: ")

            comando = """
                UPDATE animais
                SET nome = %s, especie = %s, raca = %s, idade = %s, nome_dono = %s
                WHERE id = %s
            """
            valores = (nome, especie, raca, idade, nome_dono, id_animal)
            cursor.execute(comando, valores)
            conexao.commit()

            if cursor.rowcount == 0:
                print("Nenhum animal encontrado com esse ID.")
            else:
                print("Animal atualizado com sucesso!")
        except Exception as erro:
            print(f"Erro ao atualizar animal: {erro}")
        finally:
            cursor.close()
            conexao.close()

def deletar_animal():
    """Deleta um animal pelo ID, exibindo a lista antes."""
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        try:
            cursor.execute("SELECT * FROM animais ORDER BY id ASC")
            resultados = cursor.fetchall()

            print("\n--- Animais disponíveis para deletar ---")
            for animal in resultados:
                print(f"ID: {animal[0]} | Nome: {animal[1]} | Espécie: {animal[2]}")

            id_animal = input("\nDigite o ID do animal que deseja deletar: ")

            comando = "DELETE FROM animais WHERE id = %s"
            cursor.execute(comando, (id_animal,))
            conexao.commit()

            if cursor.rowcount == 0:
                print("Nenhum animal encontrado com esse ID.")
            else:
                print("Animal deletado com sucesso!")
        except Exception as erro:
            print(f"Erro ao deletar animal: {erro}")
        finally:
            cursor.close()
            conexao.close()

def buscar_animal_por_id(id_animal):
    """Busca um animal pelo ID, imprime os dados e retorna a tupla com os dados."""
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        try:
            comando = "SELECT * FROM animais WHERE id = %s"
            cursor.execute(comando, (id_animal,))
            resultado = cursor.fetchone()

            if resultado:
                print("\n--- Animal encontrado ---")
                print(f"ID: {resultado[0]}")
                print(f"Nome: {resultado[1]}")
                print(f"Espécie: {resultado[2]}")
                print(f"Raça: {resultado[3]}")
                print(f"Idade: {resultado[4]}")
                print(f"Dono: {resultado[5]}")
                return resultado
            else:
                print("Nenhum animal encontrado com esse ID.")
                return None
        except Exception as erro:
            print(f"Erro ao buscar animal: {erro}")
            return None
        finally:
            cursor.close()
            conexao.close()
