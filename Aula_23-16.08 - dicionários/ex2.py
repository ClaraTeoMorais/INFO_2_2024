import json

class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"

def salvar():
    a = Cliente(1, "Douglas Crockford")
    b = Cliente(2, "Jon Bosak")

    # print(a)
    # print(b)
    # print(a.__dict__) #adiciona os itens em um dicionário
    # print(vars(b)) # cria um dicionário (mesma coisa que o __dict__)

    lista = [a,b]

    with open("clientes.json", mode="w") as arquivo:    # w = write
        json.dump(lista,arquivo,defaul = vars)   # o dump pega a lista e converte todos em dicionário
    # open = abrir arquivo 
    # quando usa o with, ao terminar o bloco, ele fecha automaticamente o arquivo


# salvar()

def abrir():
    lista = []
    with open("clientes.json", mode="r") as arquivo:    # r = read
        texto = json.load(arquivo)
        for obj in texto:   
            c = Cliente(obj["id"], obj["nome"])
            lista.append(c)
        for Cliente in lista:
            print(Cliente)