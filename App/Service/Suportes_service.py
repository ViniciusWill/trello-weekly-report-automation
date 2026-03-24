def formatar_planilha_suporte(writer, df_final, nome_planilha, titulo_planilha, cor):
    print(f"Formatando planilha SUPORTE: {nome_planilha}...")
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
    formato_porcentagem = workbook.add_format({'num_format': '0.00%', 'border': 1})
    formato_label_total = workbook.add_format({'bold': True, 'font_size': 11, 'valign': 'vcenter', 'align': 'right'})
    formato_valor_total = workbook.add_format({'bold': True, 'num_format': '0.00', 'border': 1, 'fg_color': '#FDE9D9'})
    formato_valor_media = workbook.add_format({'bold': True, 'num_format': '0.00', 'border': 1})
    formato_lateral_total_num = workbook.add_format({'bold': True, 'num_format': '0.00', 'border': 1, 'bg_color': '#D9D9D9'})
    formato_lateral_total_perc = workbook.add_format({'bold': True, 'num_format': '0.00%', 'border': 1, 'bg_color': '#D9D9D9'})

    # - Tabela Principal 
    worksheet.merge_range('A1:C1', titulo_planilha, formato_titulo)
    worksheet.write('A2', 'Descrição', formato_cabecalho)
    worksheet.write('B2', 'Membro', formato_cabecalho)
    worksheet.write('C2', 'Total Geral', formato_cabecalho)
    worksheet.set_column('A:A', 50) 
    worksheet.set_column('B:B', 25) 
    worksheet.set_column('C:C', 15) 
    worksheet.set_column('D:D', 5) 
    
    num_rows = len(df_final)
    if num_rows > 0:
        worksheet.conditional_format(2, 0, num_rows + 1, 0, {'type': 'no_blanks', 'format': formato_texto})
        worksheet.conditional_format(2, 1, num_rows + 1, 1, {'type': 'no_blanks', 'format': formato_texto})
        worksheet.conditional_format(2, 2, num_rows + 1, 2, {'type': 'no_blanks', 'format': formato_numero})
    
        linha_total_geral = num_rows + 3 
        linha_media = num_rows + 4       
        celula_inicio_C = 'C3'; celula_fim_C = f'C{num_rows + 2}'
        
        worksheet.merge_range(linha_total_geral, 0, linha_total_geral, 1, 'Total Geral', formato_label_total)
        worksheet.write_formula(linha_total_geral, 2, f'=SUM({celula_inicio_C}:{celula_fim_C})', formato_valor_total)
        
        worksheet.merge_range(linha_media, 0, linha_media, 1, 'Média', formato_label_total)
        worksheet.write_formula(linha_media, 2, f'=AVERAGE({celula_inicio_C}:{celula_fim_C})', formato_valor_media)

        # - Tabela Lateral
        try:
            df_grouped = df_final.groupby('Membro')['Total Geral'].sum().reset_index()
            df_grouped = df_grouped.sort_values(by='Total Geral', ascending=False)
            total_absoluto = df_grouped['Total Geral'].sum()
            
            if total_absoluto > 0:
                worksheet.write('E2', 'Membro (Resumo)', formato_cabecalho)
                worksheet.write('F2', 'Total Horas', formato_cabecalho)
                worksheet.write('G2', '% do Total', formato_cabecalho)
                
                worksheet.set_column('E:E', 25)
                worksheet.set_column('F:F', 15)
                worksheet.set_column('G:G', 15)
                row_idx = 2
                for index, row in enumerate(df_grouped.itertuples()):
                    row_idx = 2 + index
                    membro = row.Membro
                    valor = row._2
                    percentual = valor / total_absoluto
                    
                    worksheet.write(row_idx, 4, membro, formato_texto)      
                    worksheet.write(row_idx, 5, valor, formato_numero)       
                    worksheet.write(row_idx, 6, percentual, formato_porcentagem) 
                linha_tot_lat = row_idx + 1
                worksheet.write(linha_tot_lat, 4, 'Total', formato_lateral_total_num)
                worksheet.write_formula(linha_tot_lat, 5, f'=SUM(F3:F{linha_tot_lat})', formato_lateral_total_num)
                worksheet.write_formula(linha_tot_lat, 6, f'=SUM(G3:G{linha_tot_lat})', formato_lateral_total_perc)

        except Exception as e:
            print(f"Aviso: Não foi possível gerar a tabela lateral: {e}")

    worksheet.freeze_panes(2, 0)