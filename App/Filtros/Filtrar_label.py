import pandas as pd
import warnings
import numpy as np

def tratar_colunas_trello(df):
    try:
        print("Verificar Labels da planilha....")
        colunas = ['Created', 'Name', 'Member', 'Label', 'Total Time', 'Current List', 'Time in Em desenvolvimento']
        if not all(c in df.columns for c in colunas): raise ValueError("Colunas em falta.")
        df['Label_Logic'] = df['Label'].fillna('Sem Etiqueta').astype(str).str.strip().str.lower()
        df['CurrentList_Logic'] = df['Current List'].fillna('Não Definido').astype(str).str.strip().str.lower()
        df['Name_Display'] = df['Name'].fillna('Sem Nome').str.strip()
        df['Member_Display'] = df['Member'].fillna('Não atribuído').str.strip()
        df['Total Time'] = pd.to_numeric(df['Total Time'], errors='coerce').fillna(0)
        df['Time in Em desenvolvimento'] = pd.to_numeric(df['Time in Em desenvolvimento'], errors='coerce').fillna(0)
       ##
        with warnings.catch_warnings():
         warnings.simplefilter("ignore")
        df['Data'] = pd.to_datetime(df['Created'], format='%b %d, %Y', errors='coerce')
    except Exception as e:
        print(f"ERRO processamento: {e}")
    
    return df
    
def separacao_tipo_solicitação(df):
    mask_suporte = df['CurrentList_Logic'].str.contains('suportes realizados', na=False)
    df_suportes = df[mask_suporte].copy()
    mask_concluido = df['CurrentList_Logic'].str.contains('concluído', na=False)
    df_base_concluidos = df[mask_concluido & ~mask_suporte].copy()
    mask_bug_label = df_base_concluidos['Label_Logic'].str.contains('bug', na=False)
    df_bug = df_base_concluidos[mask_bug_label].copy()
    df_melhorias = df_base_concluidos[~mask_bug_label].copy()
    
    print(f"Resumo da separação:")
    print(f" - Suportes: {len(df_suportes)}")
    print(f" - Bugs (Status Concluído): {len(df_bug)}")
    print(f" - Melhorias (Status Concluído): {len(df_melhorias)}")

    return df_suportes, df_bug, df_melhorias

def preparar_dataframes_finais(df_suportes, df_bug, df_melhorias):
    # Suportes
    df_s_fin = df_suportes.rename(columns={
        'Name_Display': 'Descrição',
        'Member_Display': 'Membro',
        'Total Time': 'Total Geral (hr)'
    })[['Descrição', 'Membro', 'Total Geral (hr)']]

    # Bugs
    df_b_fin = df_bug.copy()
    df_b_fin['Time in Em desenvolvimento'] = np.minimum(df_b_fin['Total Time'], df_b_fin['Time in Em desenvolvimento'])
    df_b_fin['Total - Dev'] = df_b_fin['Total Time'] - df_b_fin['Time in Em desenvolvimento']
    df_b_fin = df_b_fin.rename(columns={
    'Name_Display': 'Descrição',
    'Member_Display': 'Membro',
    'Total Time': 'Total Geral',
    'Total - Dev': 'Total - Tempo em Desenvolvimento'
    })[['Descrição', 'Membro', 'Total Geral', 'Total - Tempo em Desenvolvimento']]

    # Melhorias
    df_m_fin = df_melhorias.copy()
    df_m_fin['Time in Em desenvolvimento'] = np.minimum(df_m_fin['Total Time'], df_m_fin['Time in Em desenvolvimento'])
    df_m_fin['Total - Dev'] = df_m_fin['Total Time'] - df_m_fin['Time in Em desenvolvimento']
    df_m_fin = df_m_fin.rename(columns={
    'Name_Display': 'Descrição',
    'Member_Display': 'Membro',
    'Total Time': 'Total HR',
    'Total - Dev': 'Total - Tempo em Desenvolvimento'
    })[['Descrição', 'Membro', 'Total HR', 'Total - Tempo em Desenvolvimento']]

    return df_s_fin, df_b_fin, df_m_fin