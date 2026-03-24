   

def bugs_invalidos(df):
    print("Verificando observações....")
    nomes_lower = df['Name'].str.lower()
    buginvalido = nomes_lower.str.contains(r'\(n[ãa]o [ée] bug\)', regex=True)  
    buginvalidomelhoria = nomes_lower.str.contains(r'\(melhoria\)', regex=True)
    if buginvalido.any() or buginvalidomelhoria.any():
     print('Encontrado solicitação de bug invalida.')
     print(f" -> Zerando tempo de {buginvalido.sum()} itens marcados como '(não é bug)'.")
     df.loc[buginvalido, 'Total Time'] = 0  
     df.loc[buginvalido, 'Time in Em desenvolvimento'] = 0
    else:
     print("Nenhum bug inválido encontrado.")
    return df 
