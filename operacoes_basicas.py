import pandas as pd


df = pd.read_csv("tabela_pbf.csv")
print(df)

# deletar uma coluna do DataFrame
df.drop("Unnamed: 0", axis=1, inplace=True)
print(f'\n\n{df}')

# criar uma nova coluna
df["Parcela Atualizada"] = df["VALOR PARCELA"] + df["VALOR PARCELA"] * 0.1
print(f'\n\n{df}')

# trabalhando com linhas
print(f'\n\n{df.loc[0:5, ["NOME MUNICÍPIO", "UF", "Parcela Atualizada"]]}')

# filtrar
df_to = df.loc[df["UF"] == "TO"]
tupiratins = df_to[df["NOME MUNICÍPIO"] == "TUPIRATINS"]
valor_tupiratins = tupiratins["VALOR PARCELA"].sum()
print(f'Total pagos em Tupiratins:\nR$ {valor_tupiratins:.2f}')

# deletar uma linha do DataFrame
df_to.drop(14233114, axis=0, inplace=True)
print(f'\n\n{df_to}')
