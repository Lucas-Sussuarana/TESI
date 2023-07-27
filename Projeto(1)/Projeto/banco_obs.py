import sqlite3
from sqlite3 import Error

def conexao():
    caminho = "C:\\Users\\lucas\\Databasesql\\bancodoprojetoparaobs.db"
    try:
        con = None
        con = sqlite3.connect(caminho)
        return con
    except Error as error:
        print(error)

#sql_insert = 'INSERT INTO cliente VALUES(5, "ale", "00000000000");'

#sql_tabela = 'CREATE TABLE observacoes(id INTEGER PRIMARY KEY, nome VARCHAR(60) NOT NULL, cpf VARCHAR(11) NOT NULL);'

#sql_delete_id = 'DELETE FROM cliente WHERE id=1;'

#sql_atualizar = 'UPDATE cliente SET nome="SOGEKING" WHERE id=1;'

sql_consulta = 'SELECT * FROM observacoes;'



def tabela_obs(sql):
    con = conexao()
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    print("tabela Criada")
    con.close()

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

