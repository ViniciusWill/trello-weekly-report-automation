import os 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_ENTRADA = os.path.join(BASE_DIR, "Input")
PASTA_SAIDA   = os.path.join(BASE_DIR, "Output")
os.makedirs(PASTA_ENTRADA, exist_ok=True)
os.makedirs(PASTA_SAIDA,   exist_ok=True)
ARQUIVO_ENTRADA          = "trello.xlsx"
CAMINHO_ENTRADA_COMPLETO = os.path.join(PASTA_ENTRADA, ARQUIVO_ENTRADA)
COR_CABECALHO_PADRAO = '#4BACC6'