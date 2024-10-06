import pandas as pd
import streamlit as st
from etl import ler_arquivo_winfut

df = ler_arquivo_winfut('data/winfut1min.xlsx')
df_resultado = ler_arquivo_winfut('data/resultado.xlsx')

#Título do Dash
st.title('Dashboard dos resultados do modelo operacional')

#Filter de data 
st.sidebar.header('Filtro data resultados')
start_date = st.sidebar.date_input('Data Inicio', df_resultado['Dia'].min())
end_date = st.sidebar.date_input('Data Final', df_resultado['Dia'].max())