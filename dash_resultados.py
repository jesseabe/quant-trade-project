import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from etl import ler_arquivo_winfut
from estrategia import processar_multiplos_dias

df = ler_arquivo_winfut('data/winfut1min.xlsx')
df_resultado = ler_arquivo_winfut('data/resultado.xlsx')

#Título do Dash
st.title('Dashboard dos resultados do modelo operacional')

#Filtro de data
st.sidebar.header('Filtro data resultados')
start_date = st.sidebar.date_input('Data Inicio', df_resultado['Dia'].min())
end_date = st.sidebar.date_input('Data Final', df_resultado['Dia'].max())

# Aplicar filtro de datas
df_filtered = df_resultado[(df_resultado['Dia'] >= pd.to_datetime(start_date)) &
                           (df_resultado['Dia'] <= pd.to_datetime(end_date))]

# Show filtered data
st.subheader('Resultados do Modelo Operacional')
st.write(df_filtered)

# Verificar se o DataFrame filtrado contém dados
if df_filtered.empty:
    st.warning('Nenhum dado disponível para o intervalo selecionado.')
else:
    # Gráfico de montanha com o resultado acumulado ao longo do tempo
    st.subheader('Evolução Acumulada dos Resultados ao Longo do Tempo')
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.fill_between(df_filtered['Dia'], 
                    df_filtered['Resultado_Acumulado'], 
                    color='skyblue', alpha=0.4)
    ax.plot(df_filtered['Dia'], df_filtered['Resultado_Acumulado'], color='blue', alpha=0.6)
    
    ax.set_title('Evolução Acumulada dos Resultados ao Longo do Tempo', fontsize=14)
    ax.set_xlabel('Tempo (Dia)', fontsize=12)
    ax.set_ylabel('Resultado Acumulado', fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True)
    
    st.pyplot(fig)