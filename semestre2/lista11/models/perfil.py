import json
from models.crud import CRUD

class Perfil:
  def __init__(self, id, nome, descricao, beneficio):
    self.id = id
    self.nome = nome
    self.descricao = descricao
    self.beneficio = beneficio
  def __str__(self):
    return f"{self.id} - {self.nome} - {self.descricao} - {self.beneficio}"

class Perfis(CRUD):

  def atualizar(self, obj):
    c = self.listar_id(obj.id)
    if c != None:
      c.nome = obj.nome
      c.descricao = obj.descricao
      c.beneficio = obj.beneficio
      self.salvar()

  def salvar(self):
    with open("perfis.json", mode="w") as arquivo:   # w - write
      json.dump(self.objetos, arquivo, default = vars)

  def abrir(self):
    self.objetos = []
    try:
      with open("perfis.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Perfis(obj["id"], obj["nome"], obj["descricao"], obj["beneficio"])
          self.objetos.append(c)
    except FileNotFoundError:
      pass

