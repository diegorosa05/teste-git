import json
import pandas as pd

with open('faturamento.json', 'r') as f:
    dia = json.load(f)

df = pd.DataFrame(dia['faturamento_diario'])

df_faturamento = df.loc[df['valor'] != 0]
min_faturamento = df['valor'].min()
max_faturamento = df['valor'].max()
media_faturamento = df['valor'].mean()
dias_acima_da_media = len(df[df['valor'] > media_faturamento])

print(f'Menor valor de faturamento: {min_faturamento}')
print(f'Maior valor de faturamento: {max_faturamento}')
print(f'Número de dias com faturamento acima da média: {dias_acima_da_media}')
