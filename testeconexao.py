from app.db import conectar

conexao = conectar()
if conexao:
    print("Conexão realizada com sucesso!")
    conexao.close()
else:
    print("Falha na conexão.")
