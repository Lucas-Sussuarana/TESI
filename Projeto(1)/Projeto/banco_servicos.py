import sqlite3
from sqlite3 import Error

def conexao():
    caminho = "C:\\Users\\lucas\\Databasesql\\bancodoprojeto.db"
    try:
        con = None
        con = sqlite3.connect(caminho)
        return con
    except Error as error:
        print(error)

sql_consulta = 'SELECT * FROM cliente;'
sql_consulta_obs = 'SELECT * FROM veiculo;'
sql_consulta_pecas = 'SELECT * FROM pecas'
sql_consulta_servico = 'SELECT * FROM servico'

'''

A parte do banco de dados que cuidara dos clientes e suas respectivas caracteristicas lhes dando um ID, 
esses clientes não podem ser excluidos pois pode gerar falhas no catalogo dos ID's,
sem falar que não existe necessidade em excluir os clientes

'''


def inserir(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        #Verifica a conexão com 'commit'
        con.commit()
        print('Registro inserido com sucesso!')
        con.close()
    except Error as er:
        print(er)


def delete_id(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print("Deletado com sucesso")
        con.close()
    except Error as er:
        print(er)

def atualizar_id(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print("Resgistro atualizado com sucesso")
        con.close()
    except Error as er:
        print(er)
def consultar_tabela(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        con.close()
        return resultado
    except Error as er:
        print(er)


'''

A parte que cuida da tabela onde sera adicionado os veiculos atrelado ao ID dos clientes, tendo em vista que o id de cliente não pode ser excluido

'''

def inserir_obs(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        #Verifica a conexão com 'commit'
        con.commit()
        con.close()
    except Error as er:
        print(er)


def delete_id_obs(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
    except Error as er:
        print(er)
        print(sql)

def atualizar_id_obs(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
    except Error as er:
        print(er)
def consultar_tabela_obs(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        #retorna o resultado da execução do sql
        resultado = cursor.fetchall()
        con.close()
        return resultado
    except Error as er:
        print(er)
