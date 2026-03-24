import locale
import time
import os
import pandas as pd

def trello_reader(caminho_entrada_completo):
    try: locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
    except locale.Error: 
        try: locale.setlocale(locale.LC_TIME, 'en_US')
        except: print("Aviso: Locale padrão.")

    if not os.path.exists(caminho_entrada_completo):
        print(f"ERRO: Arquivo não encontrado em: {caminho_entrada_completo}")
        return 
    try:
        df = pd.read_excel(caminho_entrada_completo, header=1) 
    except Exception as e:
        print(f"ERRO ao ler Excel: {e}")
        return
    print(f"Arquivo encontrado. Aguardando 2 segundos...")
    time.sleep(2) 
    return df


