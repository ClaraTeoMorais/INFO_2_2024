from models.crud import CRUD

import json

class Cliente:
  def __init__(self, id, nome, email, fone, senha, id_perfil):
    self.id = id
    self.nome = nome
    self.email = email
    self.fone = fone
    self.senha = senha
    self.id_perfil = id_perfil
  def __str__(self):
    return f"{self.nome} - {self.email} - {self.fone}"

class Clientes(CRUD):
    
  def atualizar(self, obj):
    c = self.listar_id(obj.id)
    if c != None:
      c.nome = obj.nome
      c.email = obj.email
      c.fone = obj.fone
      c.senha = obj.senha
      c.id_perfil = obj.id_perfil
      self.salvar()
  
  @classmethod
  def listar(self):
    self.abrir()
    self.objetos.sort(key=lambda cliente: cliente.nome)
    return self.objetos

  @classmethod
  def salvar(self):
    with open("clientes.json", mode="w") as arquivo:   # w - write
      json.dump(self.objetos, arquivo, default = vars)

  @classmethod
  def abrir(self):
    self.objetos = []
    try:
      with open("clientes.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"], obj["id_perfil"])
          self.objetos.append(c)
    except FileNotFoundError:
      pass

