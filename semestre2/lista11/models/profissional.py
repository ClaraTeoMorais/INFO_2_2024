import json
from models.crud import CRUD

# Modelo
class Profissional:
  def __init__(self, id, nome, especialidade, conselho, email, senha):
    self.id = id
    self.nome = nome
    self.especialidade = especialidade
    self.conselho = conselho
    self.email = email
    self.senha = senha
  def __str__(self):
    return f"{self.nome} - {self.especialidade} - {self.conselho}"

class Profissionais(CRUD):

  def atualizar(self, obj):
    c = self.listar_id(obj.id)
    if c != None:
      c.nome = obj.nome
      c.especialidade = obj.especialidade
      c.conselho = obj.conselho
      c.email = obj.email
      c.senha = obj.senha
      self.salvar()

  def salvar(self):
    with open("profissionais.json", mode="w") as arquivo:   # w - write
      json.dump(self.objetos, arquivo, default = vars)

  def abrir(self):
    self.objetos = []
    try:
      with open("profissionais.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Profissional(obj["id"], obj["nome"], obj["especialidade"], obj["conselho"])
          self.objetos.append(c)
    except FileNotFoundError:
      pass

