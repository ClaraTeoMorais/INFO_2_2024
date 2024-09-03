from datetime import datetime

# Exemplo de lista de datas
datas = [
    datetime(2023, 5, 17),
    datetime(2021, 8, 22),
    datetime(2022, 12, 5),
    datetime(2023, 1, 15)
]

# Ordenando a lista de datas em ordem crescente
datas_ordenadas = sorted(datas)

# Exibindo o resultado
for data in datas_ordenadas:
    print(data.strftime("%d/%m/%Y"))