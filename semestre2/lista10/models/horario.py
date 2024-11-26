import json
from datetime import datetime

class Horario:
  def __init__(self, id, data):
    self.__id = id
    self.__data = data
    self.__confirmado = False
    self.__id_cliente = 0
    self.__id_servico = 0

  def set_id(self, h):
    if h != "":
      self.__id = h
    else:
      raise ValueError()

  def get_id(self):
    return self.__id

  def set_data(self, h):
    if h != "":
      self.__data = h
    else:
      raise ValueError()

  def get_data(self):
    return self.__data

  def set_confirmado(self, h):
    if h != "":
      self.__confirmado = h
    else:
      raise ValueError()

  def get_confirmado(self):
    return self.__confirmado

  def set_id_cliente(self, h):
    if h != "":
      self.__id_cliente = h
    else:
      raise ValueError()

  def get_id_cliente(self):
    return self.__id_cliente

  def set_id_servico(self, h):
    if h != "":
      self.__id_servico = h
    else:
      raise ValueError()

  def get_id_servico(self):
    return self.__id_servico
  
  def __str__(self):
    return f"{self.__id} - {self.__data}"
  def to_json(self):
    dic = {}
    dic["self.__id"] = self.__id
    dic["self.__data"] = self.__data.strftime("%d/%m/%Y %H:%M")
    dic["self.__confirmado"] = self.__confirmado
    dic["self.__id_cliente"] = self.__id_cliente
    dic["self.__id_servico"] = self.__id_servico
    return dic    

class Horarios:
  objetos = []    # atributo estático

  @classmethod
  def inserir(self, obj):
    self.abrir()
    m = 0
    for c in self.objetos:
      if c.get_id() > m: 
        m = c.get_id()
    obj.id = m + 1
    self.objetos.append(obj)
    self.salvar()

  @classmethod
  def listar_id(self, id):
    self.abrir()
    for c in self.objetos:
      if c.get_id() == id: 
        return c
    return None  
  
  @classmethod
  def atualizar(self, obj):
    c = self.listar_id(obj.id)
    if c != None:
      c.self.__data = obj.self.__data
      c.self.__confirmado = obj.confirmado
      c.self.__id_cliente = obj.id_cliente
      c.self.__id_servico = obj.id_servico
      self.salvar()

  @classmethod
  def excluir(self, obj):
    c = self.listar_id(obj.id)
    if c != None:
      self.objetos.remove(c)
      self.salvar()
  
  @classmethod
  def listar(self):
    self.abrir()
    return self.objetos
  
  @classmethod
  def salvar(self):
    with open("horarios.json", mode="w") as arquivo:   # w - write
      json.dump(self.objetos, arquivo, default = Horario.to_json)

  @classmethod
  def abrir(self):
    self.objetos = []
    try:
      with open("horarios.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Horario(obj["id"], datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"))
          c.self.__confirmado = obj["confirmado"]
          c.self.__id_cliente = obj["id_cliente"]
          c.self.__id_servico = obj["id_servico"]
          self.objetos.append(c)
    except FileNotFoundError:
      pass



