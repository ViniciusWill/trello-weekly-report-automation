
def formatar_planilha_bug(writer, df_final, nome_planilha, titulo_planilha, cor):
    """Aplica o layout de LISTA PLANA (Bugs) com totalizadores."""
    print(f"Formatando planilha BUG: {nome_planilha}...")
    workbook = writer.book
    try:
        worksheet = workbook.add_worksheet(nome_planilha)
    except:
        worksheet = writer.sheets[nome_planilha]
    
    # - Formatos 
    formato_titulo = workbook.add_format({'bold': True, 'font_size': 18, 'valign': 'vcenter'})
    formato_cabecalho = workbook.add_format({'bold': True, 'fg_color': cor, 'font_color': 'white', 'border': 1, 'valign': 'vcenter', 'align': 'center'})
    formato_texto = workbook.add_format({'border': 1})
    formato_numero = workbook.add_format({'num_format': '0.00', 'border': 1})
    formato_label_total = workbook.add_format({'bold': True, 'font_size': 11, 'valign': 'vcenter', 'align': 'right'})
    formato_valor_total = workbook.add_format({'bold': True, 'num_format': '0.00', 'border': 1, 'fg_color': '#FDE9D9'})
    formato_valor_media = workbook.add_format({'bold': True, 'num_format': '0.00', 'border': 1})

     # - Tabela Principal 
    worksheet.merge_range('A1:E1', titulo_planilha, formato_titulo)
    worksheet.write('A2', 'Descrição', formato_cabecalho); worksheet.write('B2', 'Membro', formato_cabecalho)
    worksheet.write('C2', 'Total Geral', formato_cabecalho); worksheet.write('D2', 'Total - Tempo em Desenvolvimento', formato_cabecalho)
    worksheet.set_column('A:A', 50); worksheet.set_column('B:B', 25); worksheet.set_column('C:C', 15)
    worksheet.set_column('D:D', 30); worksheet.set_column('E:E', 30)

    num_rows = len(df_final)
    if num_rows > 0:
        worksheet.conditional_format(2, 0, num_rows + 1, 0, {'type': 'no_blanks', 'format': formato_texto})
        worksheet.conditional_format(2, 1, num_rows + 1, 1, {'type': 'no_blanks', 'format': formato_texto})
        worksheet.conditional_format(2, 4, num_rows + 1, 4, {'type': 'no_blanks', 'format': formato_texto})
        worksheet.conditional_format(2, 2, num_rows + 1, 2, {'type': 'no_blanks', 'format': formato_numero})
        worksheet.conditional_format(2, 3, num_rows + 1, 3, {'type': 'no_blanks', 'format': formato_numero})

        linha_total_geral = num_rows + 3; linha_media = num_rows + 4       
        celula_inicio_C = 'C3'; celula_fim_C = f'C{num_rows + 2}'
        formula_soma_C = f'=SUM({celula_inicio_C}:{celula_fim_C})'; formula_media_C = f'=AVERAGE({celula_inicio_C}:{celula_fim_C})'
        celula_inicio_D = 'D3'; celula_fim_D = f'D{num_rows + 2}'
        formula_soma_D = f'=SUM({celula_inicio_D}:{celula_fim_D})'; formula_media_D = f'=AVERAGE({celula_inicio_D}:{celula_fim_D})'

        worksheet.merge_range(linha_total_geral, 0, linha_total_geral, 1, 'Total Geral', formato_label_total)
        worksheet.write_formula(linha_total_geral, 2, formula_soma_C, formato_valor_total)
        worksheet.write_formula(linha_total_geral, 3, formula_soma_D, formato_valor_total)
        worksheet.merge_range(linha_media, 0, linha_media, 1, 'Média', formato_label_total)
        worksheet.write_formula(linha_media, 2, formula_media_C, formato_valor_media)
        worksheet.write_formula(linha_media, 3, formula_media_D, formato_valor_media)
        
    worksheet.freeze_panes(2, 0)
