import json

class Servico:
    def __init__(self, id, descricao, valor, duracao):
        self.id = id
        self.d = descricao
        self.v = valor
        self.t = duracao

    def __str__(self):
        return print(f"{self.id} - {self.d} - {self.v} - {self.t}")

class Servicos:
    objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for s in cls.objetos:
            if s.id > m:
                m = s.id
        obj.id = m + 1
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for s in cls.objetos:
            if s.id == id:
                return s
        return None
    
    @classmethod
    def atualizar(cls, obj):
        s = cls.listar_id(obj.id)
        if s != None:
            s.d = obj.descricao
            s.v = obj.valor
            s.t = obj.duracao
            cls.salvar()
    
    @classmethod
    def excluir(cls, obj):
        s = cls.listar_id(obj.id)
        if s != None:
            cls.objetos.remove(s)
            cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("servico.json", mode="r") as arquivo:  
                texto = json.load(arquivo)
                for obj in texto:   
                    s = Servico(obj["id"], obj["descricao"], obj["valor"], obj["duracao"])
                    cls.objetos.append(s)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("servico.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)