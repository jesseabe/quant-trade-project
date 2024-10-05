import pandas as pd

# Função que realiza a leitura do arquivo

def ler_arquivo_winfut(caminho):
    df = pd.read_excel(caminho)
    return df 

def tranformacao_winfut(df: pd.DataFrame)-> pd.DataFrame:
    df = df.copy()
    df['Oscilacao'] = df['Máxima'] - df['Mínima']
    df['%Var_Ab_Fec'] = (df['Abertura'] - df['Fechamento'])/df['Abertura']
    df['Dif_Ab_Fec'] = df['Abertura'] - df['Fechamento']
    df['Dif_Max_Fec'] = df['Máxima'] - df['Fechamento']
    df['Dif_Min_Fec'] = df['Fechamento'] - df['Mínima']
    df['Dif_Ab_Max'] = df['Máxima'] - df['Abertura']
    df['Dif_Ab_Min'] = df['Abertura'] - df['Mínima']
    print(df.head())
    return df 

def calcula_metricas(df):
    pass

def plot_line_graph(df, columnX, columnY):
    pass

def plot_bar_graph(df, column):
    pass





if __name__ == "__main__":
    winfut1min = ler_arquivo_winfut('data/winfut1min.xlsx')
    winfut5min = ler_arquivo_winfut('data/winfut5min.xlsx')
    winfut15min = ler_arquivo_winfut('data/winfut15min.xlsx')
    winfut60min = ler_arquivo_winfut('data/winfut60min.xlsx')
    winfut1min_transformado = tranformacao_winfut(winfut1min)
    winfut5min_transformado = tranformacao_winfut(winfut5min)
    winfut15min_transformado = tranformacao_winfut(winfut15min)
    winfut60min_transformado = tranformacao_winfut(winfut60min)
