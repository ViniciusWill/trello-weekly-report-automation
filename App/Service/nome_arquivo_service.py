import os
from datetime import datetime    

def nome_novo_arquivo(pasta_saida):
    nome_saida = f"MELHORIAS, BUGS E SUPORTES - {datetime.now().strftime('%Y.%W')}.xlsx"
    caminho_saida = os.path.join(pasta_saida, nome_saida)
    print(f"Salvando em: {nome_saida}")
    return caminho_saida