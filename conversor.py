import pandas as pd
import sqlite3
from etl import ler_arquivo_winfut

def xslx_to_sql(df, table_name, db_path):
    """Conecta ao banco de dados SQLite e salva os dados."""
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

if __name__ == "__main__":
    # Lê o arquivo XLSX usando a função personalizada
    df = ler_arquivo_winfut('data/winfut1min.xlsx')

    # Chama a função para carregar o DataFrame no SQL
    xslx_to_sql(df, 'winfut1min', 'data/winfut1min.db')


