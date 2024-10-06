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
    print(f'Média de Oscilação', df['Oscilacao'].mean())
    print(f'Desvio Padrão Oscilação', df['Oscilacao'].std())
    print(f'Média da Dif. entre Abertura e Fechamento', df['Dif_Ab_Fec'].mean())
    print(f'Média da Dif. entre Máxima e Fechamento', df['Dif_Max_Fec'].mean())
    print(f'Média da Dif. entre Mínima e Fechamento', df['Dif_Min_Fec'].mean())
