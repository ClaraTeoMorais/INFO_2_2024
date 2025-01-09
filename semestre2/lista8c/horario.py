import json
from datetime import datetime

class Horario:
    def __init__(self, id, data):
        self.id = id
        self.d = data
        self.confirmado = False
        self.id_cliente = 0
        self.id_servico = 0

    def __str__(self):
        return print(f"{self.id} - {self.d}")

    def to__json(self):
        dic = {}
        dic["id"] = self.id
        dic["data"] = self.data.strftime("%d/%m/%Y %H:%M")
        dic["confirmado"] = self.confirmado
        dic["id_cliente"] = self.id_cliente
        dic["servico"] = self.servico


class Horarios:
    objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for h in cls.objetos:
            if h.id > m:
                m = h.id
        obj.id = m + 1
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for h in cls.objetos:
            if h.id == id:
                return h
        return None
    
    @classmethod
    def atualizar(cls, obj):
        h = cls.listar_id(obj.id)
        if h != None:
            h.d = obj.data
            h.confirmado = obj.confirmado
            h.id_cliente = obj.id_cliente
            h.id_servico = obj.id_servico
            cls.salvar()
    
    @classmethod
    def excluir(cls, obj):
        h = cls.listar_id(obj.id)
        if h != None:
            cls.objetos.remove(h)
            cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
    def abrir_agenda(cls):
        cls.abrir()
        obj = []
        dt = datetime.datetime.now()
        hoje = datetime.datetime(dt.day, dt.month, dt.year)
        for dt in cls.objetos:
            if not dt.self.confirmado and dt.self.d > hoje:
                obj.append(dt)
        return obj


    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("horario.json", mode="r") as arquivo:  
                texto = json.load(arquivo)
                for obj in texto:   
                    h = Horario(obj["id"], datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"))
                    h.confirmado = obj["confirmado"]
                    h.id_cliente = obj["id_cliente"]
                    h.id_servico = obj["id_servico"]
                    cls.objetos.append(h)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("horario.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Horario.to__json)