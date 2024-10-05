import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

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
    media_oscilacao = df['Oscilacao'].mean()
    std_oscilacao = df['Oscilacao'].std()
    media_dif_ab_fec = df['Dif_Ab_Fec'].mean()
    media_dif_max_fec = df['Dif_Max_Fec'].mean()
    media_dif_min_fec = df['Dif_Min_Fec'].mean()
    metricas = [media_oscilacao, std_oscilacao, media_dif_ab_fec, media_dif_max_fec, media_dif_min_fec]
    print(metricas)
    return metricas



def plot_hist(df, column, numero_bins):
    plt.figure(figsize=(12,8))
    plt.style.use('_mpl-gallery')
    plt.hist(df[column], bins=numero_bins, linewidth=0.5, edgecolor="white")
    plt.show()



def plot_boxplot(df, column):
    pass




if __name__ == "__main__":
    # winfut1min = ler_arquivo_winfut('data/winfut1min.xlsx')
    # winfut5min = ler_arquivo_winfut('data/winfut5min.xlsx')
    # winfut15min = ler_arquivo_winfut('data/winfut15min.xlsx')
    winfut60min = ler_arquivo_winfut('data/winfut60min.xlsx')
    # winfut1min_transformado = tranformacao_winfut(winfut1min)
    # winfut5min_transformado = tranformacao_winfut(winfut5min)
    # winfut15min_transformado = tranformacao_winfut(winfut15min)
    winfut60min_transformado = tranformacao_winfut(winfut60min)
    # winfut1min_metricas = calcula_metricas(winfut1min_transformado)
    winfut60min_metricas = calcula_metricas(winfut60min_transformado)
    plot_oscilacao_winfut60min = plot_hist(winfut60min_transformado, 'Oscilacao', 20)