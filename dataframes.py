import pandas as pd
import numpy as np

dados = {
    "nome": ["Alailda", "Helton", "Rosilene", "João Victor", "Rebecca"],
    "idade": [64, 39, 42, 13, 12],
    "naturalidade": [
        "Alagoinhas - BA",
        "Aracaju - SE",
        "Conceição do Araguaia - PA",
        "Porto Nacional - TO",
        "Porto Nacional - TO"
        ]
}

# converter os dados de um dicionário em um DataFrame
df = pd.DataFrame(dados)
print(df)

# criando DataFrame à partir de uma rede numpy
array = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)

df = pd.DataFrame(array, columns=["A", "B", "C"])
print(f'\n{df}')
