# 1. Após a abertura do mercado, pega a máxima e a mínima a cada novo candle. 
# 2. Quando a diferença entre a máxima e mínima atingir 150 pontos, caso o candle for de alta tomar uma posicao comprado, se o candle for de baixa entrar vendido. 
# 3. O alvo da operação é 300 pontos. Se atingir o alvo encerrar a posição, armazenar o resultado em um df e não abrir mais nenhuma posição no dia. 
# 4. Caso o mercado ande 150 pontos contra a posicao, inverter a mao (1 inversao) - Exemplo: Se estou comprado em 1, quero entrar vendido em 1 e armazenar o prejuízo do primeiro stop.
# 5. Caso o mercado ande novamente 150 pontos contra a posicao, inverter a mao novamente (2 inversao) - Exemplo: Se estou vendido em 1, quero entrar comprado em 1 e armazenar o prejuízo do segundo stop.
# 6. Encerrar o dia se atingir o alvo em uma das tres operações ou se tomar os tres stops. Armazenar o resultado do dia com o seguinte calculo resultado = gain ou stop em pontos * 0.2 * 5

import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = pd.read_excel('data/winfut1min.xlsx')

# Convertendo para DataFrame
df = pd.DataFrame(data)

# Convertemos a coluna 'Data' para datetime
df['Data'] = pd.to_datetime(df['Data'])

def estrategia_trading(df):
    posicao = None  # Nenhuma posição inicialmente
    resultado_dia = 0  # Resultado do dia
    maximo, minimo = None, None  # Máxima e mínima do candle
    preco_entrada = 0  # Preço da entrada
    stop_count = 0  # Contagem de stops (até 3)
    alvo = 300  # Alvo de pontos
    stop = 150  # Stop de pontos

    resultados = []  # Armazena os resultados por candle e, ao final do dia, será o resultado final

    for i, row in df.iterrows():
        # Atualizar máxima e mínima
        if maximo is None or row["Máxima"] > maximo:
            maximo = row["Máxima"]
        if minimo is None or row["Mínima"] < minimo:
            minimo = row["Mínima"]

        # Verificar se diferença entre máxima e mínima atingiu 150 pontos
        if (maximo - minimo) >= 150:
            # Se ainda não estamos posicionados
            if posicao is None:
                if row["Fechamento"] > row["Abertura"]:
                    posicao = "comprado"
                    preco_entrada = row["Fechamento"]
                elif row["Fechamento"] < row["Abertura"]:
                    posicao = "vendido"
                    preco_entrada = row["Fechamento"]
            else:
                # Se estamos comprados
                if posicao == "comprado":
                    if row["Fechamento"] >= preco_entrada + alvo:
                        resultado_dia += alvo * 0.2 * 5
                        resultados.append({"Candle": row["Data"], "Resultado": resultado_dia})
                        break  # Encerrar posição ao atingir o alvo
                    elif row["Fechamento"] <= preco_entrada - stop:
                        # Inverter posição (stop 1)
                        stop_count += 1
                        resultado_dia += -stop * 0.2 * 5
                        posicao = "vendido"
                        preco_entrada = row["Fechamento"]
                        if stop_count >= 3:
                            resultados.append({"Candle": row["Data"], "Resultado": resultado_dia})
                            break  # Encerrar o dia após 3 stops

                # Se estamos vendidos
                elif posicao == "vendido":
                    if row["Fechamento"] <= preco_entrada - alvo:
                        resultado_dia += alvo * 0.2 * 5
                        resultados.append({"Candle": row["Data"], "Resultado": resultado_dia})
                        break  # Encerrar posição ao atingir o alvo
                    elif row["Fechamento"] >= preco_entrada + stop:
                        # Inverter posição (stop 1)
                        stop_count += 1
                        resultado_dia += -stop * 0.2 * 5
                        posicao = "comprado"
                        preco_entrada = row["Fechamento"]
                        if stop_count >= 3:
                            resultados.append({"Candle": row["Data"], "Resultado": resultado_dia})
                            break  # Encerrar o dia após 3 stops

    # Se chegarmos ao final do dia sem atingir alvo ou 3 stops, armazenar o resultado final
    if stop_count < 3 and posicao is not None:
        resultados.append({"Candle": row["Data"], "Resultado": resultado_dia})

    return pd.DataFrame(resultados)

# Processar a estratégia para cada dia individualmente
def processar_multiplos_dias(df):
    # Extrair apenas a data (ignorar o tempo) para agrupar
    df['Dia'] = df['Data'].dt.date

    resultados_finais = []

    # Agrupar por dia e aplicar a estratégia
    for dia, grupo in df.groupby('Dia'):
        resultado_dia = estrategia_trading(grupo)
        resultado_dia['Dia'] = dia  # Adicionar a coluna do dia ao resultado
        resultados_finais.append(resultado_dia)

    # Concatenar todos os resultados diários em um único DataFrame
    return pd.concat(resultados_finais).reset_index(drop=True)

# Executar a estratégia para múltiplos dias
resultados_multiplos_dias = processar_multiplos_dias(df)

# Exibir resultados finais
print(resultados_multiplos_dias)

# Acumulando os resultados ao longo do tempo
resultados_multiplos_dias['Resultado_Acumulado'] = resultados_multiplos_dias['Resultado'].cumsum()

# Gerar gráfico de montanha (gráfico de área)
plt.figure(figsize=(10, 6))
plt.fill_between(resultados_multiplos_dias['Candle'], 
                 resultados_multiplos_dias['Resultado_Acumulado'], 
                 color='skyblue', alpha=0.4)
plt.plot(resultados_multiplos_dias['Candle'], resultados_multiplos_dias['Resultado_Acumulado'], color='Slateblue', alpha=0.6)

plt.title('Evolução Acumulada dos Resultados ao Longo do Tempo', fontsize=14)
plt.xlabel('Tempo (Candle)', fontsize=12)
plt.ylabel('Resultado Acumulado', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

resultados_multiplos_dias.to_csv('data/resultado.csv')
