import json

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
    def __str__(self):
        return f"{self.id}" - {self.nome} - {self.email} - {self.fone}"

class Clientes:
    objetos = []   # atributo estático
    @classmethod
    def inserir(cls,obj):
        cls.objetos.append(obj)