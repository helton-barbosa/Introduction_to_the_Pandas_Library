import pandas as pd

# ler o arquivo csv
# codificar em latin1
# aplicando o separador ";"
df = pd.read_csv("pbf2021.csv", encoding="latin1", sep=";")
# print(df)

# mostrar apenas as 5 primeiras linhas do arquivo
# print(f'{df.head(20)}')

# retornar uma tupla contendo o número de linhas e colunas
# em um DataFrame ou Series
# print(f'\n\n{df.shape}')


# exibir informações de cada coluna da tabela
# print(f'\n\n{df.info()}')

# converter dados de uma coluna de str para float
df['VALOR PARCELA'] = df['VALOR PARCELA'].apply(
    lambda x: float(x.replace(",", "."))
    )
# print(f'\n\n{df}')

# gerar um resumo estatístico de um DataFrame
# print(f'{df.describe()}')

# pegando o maior valor pago
print(f'\n\nMaior parcela paga:\nR$ {df["VALOR PARCELA"].max():.2f}')

# pegando o menor valor pago
print(f'\n\nMenor parcela paga:\nR$ {df["VALOR PARCELA"].min():.2f}')

# valor pago no mês de Janeiro
print(f'\n\nTotal pago em Janeiro/2021:\nR$ {df["VALOR PARCELA"].sum():.2f}')

# exportar os dados em um arquivo
df[["UF", "NOME MUNICÍPIO", "VALOR PARCELA"]].to_csv("tabela_pbf.csv")
