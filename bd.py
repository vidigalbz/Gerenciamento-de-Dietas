import mysql.connector

estrutura = """
dim_usuario =  ID, nome, cpf, peso, altura, idade, genero, atividade_fisica, tipo
fato_tipo =  ID, tipo
fato_sexo = ID, genero
fato_atividadefisica = ID, atividade_fisica

dim_dieta = ID, cpf_paciente, nome, calorias_diarias, 

dim_alimento = ID, nome, caloria, proteina, carboidrato, gordura

dim_refeicao = ID, nome, horario, id_dieta
"""

conexao = mysql.connector.connect(
            host = "localhost",
            user= "root",
            password = "acesso123",
            database = "gerenciamento_de_dietas",
                                              )
cursor = conexao.cursor()

def abrir_bd_fetchall(tipo, table, coluna, valor):
    if coluna == None:    
        cursor.execute("SELECT "+ tipo +" FROM "+ table)
        resultado = cursor.fetchall()
        return resultado
    
    else:
        cursor.execute("SELECT * FROM " + table +" WHERE " + coluna +"= %s", (valor,))
        resultado = cursor.fetchall()
        return resultado
        
def abrir_bd_fetchone(table, coluna, valor):
    cursor.execute("SELECT * FROM "+ table + " WHERE " + coluna + "= %s", (valor, ))
    resultado = cursor.fetchone()
    return resultado

def delete_bd(tabela, coluna, valor):
    cursor.execute("DELETE FROM " + tabela + " WHERE "+ coluna +"= %s", (valor, ))
    conexao.commit()
    
def like_bd(table, coluna, valor):
    cursor.execute("SELECT * FROM " + table + " WHERE "+ coluna + " LIKE %s", (valor, ))
    resultado = cursor.fetchall()
    return resultado

def pesquisar_join_bd(table, table2, coluna, coluna2, coluna3, valor):
    cursor.execute(f"SELECT * FROM {table} JOIN {table2} ON {table}.{coluna} = {table2}.{coluna2} WHERE {table2}.{coluna3} LIKE %s", (valor, ))
    resultado = cursor.fetchall()
    return resultado

def atualizar_bd(coluna, valor_coluna, id, valor_id):
    cursor.execute("UPDATE dim_" + id + " SET " + coluna + "=%s WHERE id_" + id + "=%s", (valor_coluna, valor_id))
    conexao.commit()

def valores_fatos(tabela, coluna, coluna2, valor):
    cursor.execute("SELECT " + coluna + " FROM " + tabela + " WHERE " + coluna2 + "= %s", (valor, ))
    resultado = cursor.fetchone()
    
    if resultado:
        for i in resultado:
            return i
            
def pesquisar_tudo(tabela, colunas, valor):
    cursor.execute(f"SELECT * FROM {tabela} WHERE " + " OR ".join([f"{coluna} LIKE %s" for coluna in colunas]), tuple([valor] * len(colunas)))
    resultado = cursor.fetchall()  
    return resultado

def inserir_bd(table, columns, values):
    colunas = ", ".join(columns)
    valores = ", ".join(["%s"] * len(values))     
    cursor.execute(f"INSERT INTO {table}({colunas}) VALUES({valores})",values)
    conexao.commit()

    resultado = cursor.fetchall()
    return resultado
       