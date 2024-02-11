import pandas as pd

idades = [12, 13, 39, 42, 64]

idades_pd = pd.Series(idades)

# identificador por índices
print(f'{idades_pd}')

# alterando o index
idades_pd.index = ['Rebecca', 'João Victor', 'Helton', 'Rosilene', 'Alailda']
print(f'\n{idades_pd}')

# operações aritméticas
adicao = idades_pd + 100
print(f'\nOperação: Adição\n{adicao}')

subtracao = idades_pd - 2
print(f'\nOperação: Subtração\n{subtracao}')

multiplicacao = idades_pd * 5
print(f'\nOperação: Multiplicação\n{multiplicacao}')

divisao = idades_pd / 2
print(f'\nOperação: Divisão\n{divisao}')

potenciacao = idades_pd ** 2
print(f'\nOperação: Potenciação\n{potenciacao}')

# identificador por slicing
print(f'\n{idades_pd[["Helton", "Rosilene"]]}')
print(f'\n{idades_pd[1:3]}')

# converter para float
print(f'\n{idades_pd.apply(float)}')

# converter para str
print(f'\n{idades_pd.apply(str)}')

# usando lambda para converter para string e alterar o . para ,
idades_pd_float = idades_pd.apply(float)
print(f'\n{idades_pd_float.apply(lambda x: str(x).replace(".", ","))}')
