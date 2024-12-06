import json
from datetime import datetime
from models.crud import CRUD

class Horario:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.confirmado = False
        self.id_cliente = 0
        self.id_servico = 0
        self.id_profissional = 0
    def __str__(self):
        return f"{self.id} - {self.data}"
    def to_json(self):
      dic = {}
      dic["id"] = self.id
      dic["data"] = self.data.strftime("%d/%m/%Y %H:%M")
      dic["confirmado"] = self.confirmado
      dic["id_cliente"] = self.id_cliente
      dic["id_servico"] = self.id_servico
      dic["id_profissional"] = self.id_profissional
      return dic    

class Horarios(CRUD):

  def atualizar(self, obj):
    c = self.listar_id(obj.id)
    if c != None:
      c.data = obj.data
      c.confirmado = obj.confirmado
      c.id_cliente = obj.id_cliente
      c.id_servico = obj.id_servico
      c.id_profissional = obj.id_profissional
      self.salvar()

  def salvar(self):
    with open("horarios.json", mode="w") as arquivo:   # w - write
      json.dump(self.objetos, arquivo, default = Horario.to_json)

  def abrir(self):
    self.objetos = []
    try:
      with open("horarios.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Horario(obj["id"], datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"))
          c.confirmado = obj["confirmado"]
          c.id_cliente = obj["id_cliente"]
          c.id_servico = obj["id_servico"]
          c.id_profissional = obj["id_profissional"]
          self.objetos.append(c)
    except FileNotFoundError:
      pass



