import mt5
import time

mt5.initialize()

tempo = time.time() +10

while time.time() < tempo:

    time.sleep(1)
    tick = mt5.symbol_info_tick("PETR4")
    print(f"O fechamento é {tick.last}")
    print(f"Valor de compra é {tick.ask}")
    print(f"Valor de venda é {tick.bid}")
    print("------------------------------")