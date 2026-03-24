import config
from Service import Suportes_service, melhorias_service, bugs_service, nome_arquivo_service
from  Leitura import trello_reader
from Filtros import Filtrar_label, Tratar_invalidos, Tratar_tempo_extra
import pandas as pd

def main():
    
    # - Ler arquivo
    print(f"Iniciando automação...")
    print("Buscando Arquivo..")
    df = trello_reader.trello_reader(config.CAMINHO_ENTRADA_COMPLETO)
    if df is None:
        print("Falha ao carregar o arquivo. Encerrando execução.")
        return
    print("Arquivo lido.")

    # - Trata excessões 
    df = Tratar_invalidos.bugs_invalidos(df)     
    df = Tratar_tempo_extra.verifica_tempo_extra(df) 
    df = Filtrar_label.tratar_colunas_trello(df) 

    # - Separação
    df_suportes, df_bug, df_melhorias = Filtrar_label.separacao_tipo_solicitação(df)

    # - Exportação
    arquivo_exportado = nome_arquivo_service.nome_novo_arquivo(config.PASTA_SAIDA)

    try:
       with  pd.ExcelWriter(arquivo_exportado, engine='xlsxwriter') as writer:
        df_s_fin, df_b_fin, df_m_fin = Filtrar_label.preparar_dataframes_finais(df_suportes, df_bug, df_melhorias)

        # - Aba Suportes
        df_s_fin.to_excel(writer, sheet_name='SUPORTES', startrow=1, index=False)
        Suportes_service.formatar_planilha_suporte(writer, df_s_fin, 'SUPORTES', 'Relatório de Suportes', config.COR_CABECALHO_PADRAO)

        # - Aba Bugs
        df_b_fin.to_excel(writer, sheet_name='BUG', startrow=1, index=False)
        bugs_service.formatar_planilha_bug(writer, df_b_fin, 'BUG', 'Relatório de Bugs', config.COR_CABECALHO_PADRAO)

        # - Aba Melhorias
        df_m_fin.to_excel(writer, sheet_name='MELHORIAS', startrow=1, index=False)
        melhorias_service.formatar_planilha_melhorias(writer, df_m_fin, 'MELHORIAS', 'Relatório de Melhorias', config.COR_CABECALHO_PADRAO)

        print("Arquivo salvo com sucesso.")

    except Exception as e:
        print(f"ERRO ao salvar/formatar: {e}")
        return


    # Excluir original
    # try:
    #     os.remove(config.CAMINHO_ENTRADA_COMPLETO)
    #     print("Arquivo original excluído.")
    # except Exception as e:
    #     print(f"Aviso: Não foi possível excluir o original: {e}")

if __name__ == "__main__":
    main()
    print("\nConcluído.")
