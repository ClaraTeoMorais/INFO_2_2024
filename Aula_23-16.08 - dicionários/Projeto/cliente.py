# Lista de Clientes
# C - Create - insere objetos na lista 
# R - Read - lsta os obj na lista
# U - update - atualiza 
# D - delete - deleta os obj na lista 

import json

class Cliente:
    def __init__(self,id,nome,email,fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"

class Clientes:
    objetos = []   # atributo estático 

    @classmethod
    def inserir(cls,obj):   # como é uma classe estática, troca-se o self pelo cls
        cls.objetos.append(obj)
        
    @classmethod
    def listar(cls):
        return cls.objetos
        
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos,arquivo,default= vars)
        
    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open("clentes.json", mode=r) as arquivo: 
            for obj in texto:
                c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
                cls.objetos.append(c)


a = Cliente(1, "Douglas Crockford, douglas@gmail.com")
b = Cliente(2, "Jon Bosak")

crud = Clientes() # crud - quem vai controlar a lista de clientes
crud.inserir(a)
crud.inserir(b)
for c in crud.listar():
    print (c)

# CLIENTES controla a lista CLIENTE
# 


