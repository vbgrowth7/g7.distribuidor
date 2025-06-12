import mysql.connector
from mysql.connector import Error
import streamlit as st

# Configurações do banco de dados
DB_CONFIG = {
    'host': 'database-1.cdqa6ywqs8pz.us-west-2.rds.amazonaws.com',  # Altere para o host do seu banco de dados
    'user': 'vinicius',  # Altere para seu usuário
    'password': 'batata#123#',  # Altere para sua senha
    'database': 'DISTRIBUIDORES'  # Nome do banco de dados
}

def testar_conexao():
    """Testa a conexão com o banco de dados"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            conn.close()
            return True, "Conexão bem sucedida"
    except Error as e:
        return False, f"Erro ao conectar: {str(e)}"

def selecionar_banco(nome_banco):
    """Seleciona o banco de dados a ser usado"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(f"USE {nome_banco}")
        cursor.close()
        conn.close()
        return True, "Banco de dados selecionado com sucesso"
    except Error as e:
        return False, f"Erro ao selecionar banco: {str(e)}"

def obter_dados(query, params=None):
    """Executa uma consulta SELECT e retorna os resultados como DataFrame"""
    import pandas as pd
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        df = pd.read_sql(query, conn, params=params)
        conn.close()
        return df
    except Error as e:
        st.error(f"Erro ao obter dados: {str(e)}")
        return pd.DataFrame()

def executar_query(query, params=None):
    """Executa uma query de atualização (INSERT, UPDATE, DELETE)"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        conn.commit()
        cursor.close()
        conn.close()
        return True, "Query executada com sucesso"
    except Error as e:
        return False, f"Erro ao executar query: {str(e)}" 