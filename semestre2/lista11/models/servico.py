import json
from models.crud import CRUD

class Servico:
  def __init__(self, id, descricao, valor, duracao):
    self.id = id
    self.descricao = descricao
    self.valor = valor
    self.duracao = duracao
  def __str__(self):
    return f"{self.id} - {self.descricao} - R$ {self.valor:.2f} - {self.duracao} min"

class Servicos(CRUD):

  def atualizar(self, obj):
    c = self.listar_id(obj.id)
    if c != None:
      c.descricao = obj.descricao
      c.valor = obj.valor
      c.duracao = obj.duracao
      self.salvar()

  def salvar(self):
    with open("servicos.json", mode="w") as arquivo:   # w - write
      json.dump(self.objetos, arquivo, default = vars)

  def abrir(self):
    self.objetos = []
    try:
      with open("servicos.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Servico(obj["id"], obj["descricao"], obj["valor"], obj["duracao"])
          self.objetos.append(c)
    except FileNotFoundError:
      pass

