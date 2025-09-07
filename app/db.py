import mysql.connector

def conectar():
    """Cria e retorna uma conexão com o banco de dados MySQL."""
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  #  coloque aqui a senha do seu MySQL
            database=""      # certifique-se de que esse banco existe
        )
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None

