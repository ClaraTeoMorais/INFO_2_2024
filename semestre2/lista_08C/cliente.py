import json

class Cliente:
    def __init__(self, id, nome, email, phone):
        self.id = id
        self.nome = nome
        self.email = email
        self.phone = phone

    def __str__(self):
        return print(f"{self.id} - {self.nome} - {self.email} - {self.phone}")

class Clientes:
    objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for c in cls.objetos:
            if c.id > m:
                m = c.id
        obj.id = m + 1
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for c in cls.objetos:
            if c.id == id:
                return c
        return None
    
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c.nome = obj.nome
            c.email = obj.email
            c.phone = obj.phone
            cls.salvar()
    
    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            cls.objetos.remove(c)
            cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("cliente.json", mode="r") as arquivo:  
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["phone"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("cliente.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)