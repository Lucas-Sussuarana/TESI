import sqlite3
from sqlite3 import Error

def conexao():
    caminho = "C:\\Users\\lucas\\Databasesql\\bancoparapecas.db"
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



def tabela_pecas(sql):
    con = conexao()
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    print("tabela Criada")
    con.close()

def inserir_pecas(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        #Verifica a conexão com 'commit'
        con.commit()
        #print('Registro inserido com sucesso!')
        con.close()
    except Error as er:
        print(er)


def delete_id_pecas(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print("Deletado com sucesso")
        con.close()
    except Error as er:
        print(er)

def atualizar_id_pecas(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print("Resgistro atualizado com sucesso")
        con.close()
    except Error as er:
        print(er)
def consultar_tabela_pecas(sql):
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

#tabela(sql_tabela)
#inserir_no_banco(sql_insert)
#delete_id(sql_delete_id)
#atualizar_id(sql_atualizar)
lista_cliente = []
