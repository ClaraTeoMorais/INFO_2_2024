x = {"RN" : "Natal", "PB" : "João Pessoa", "PE" : "Recife"}

print(x)
print(x["RN"][0])
print(x["PB"])

x["AM"] = "Manaus"
# se atribuir um novo valor, ele adiciona, e se atribuir um valor a um que já existe, ele substitui

# usa-se o "in" para ver se as chaves (RN, PB, PE) está no dicionário
# as chaves precisam ver únicas
# os valores (Natal, João Pessoa, ...) podem ser repetidos

