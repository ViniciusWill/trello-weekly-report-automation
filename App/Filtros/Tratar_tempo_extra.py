import re

def verifica_tempo_extra(df):
    pattern_hr  = r'\(([+-]?\d+(?:[.,]\d+)?)\s*hr?\)'  
    pattern_min = r'\(([+-]?\d+(?:[.,]\d+)?)\s*min\)'

    ajuste_hr = df['Name'].str.extract(pattern_hr, flags=re.IGNORECASE)[0]
    ajuste_hr = ajuste_hr.str.replace(',', '.').astype(float).fillna(0)
    ajuste_min = df['Name'].str.extract(pattern_min, flags=re.IGNORECASE)[0]
    ajuste_min = ajuste_min.str.replace(',', '.').astype(float).fillna(0) / 60

    df['Total Time'] = df['Total Time'] + ajuste_hr + ajuste_min
    df['Name'] = df['Name'].str.replace(pattern_hr,  '', regex=True, flags=re.IGNORECASE).str.strip()
    df['Name'] = df['Name'].str.replace(pattern_min, '', regex=True, flags=re.IGNORECASE).str.strip()

    itens_ajustados = (ajuste_hr != 0) | (ajuste_min != 0)
    if itens_ajustados.any():
        print(f"\n  {itens_ajustados.sum()} ajuste(s) de tempo aplicado(s):")
        print(f"  {'Nome':<50} {'Tempo Original':>15} {'Ajuste':>10} {'Total Final':>12}")
        print(f"  {'-'*87}")
    for _, row in df.loc[itens_ajustados].iterrows():
        ajuste = ajuste_hr[_] + ajuste_min[_]
        original = row['Total Time'] - ajuste
        print(f"  {row['Name']:<50} {original:>14.2f}h {ajuste:>+9.2f}h {row['Total Time']:>11.2f}h")
    print()
    return df