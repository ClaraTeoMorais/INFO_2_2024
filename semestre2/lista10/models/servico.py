import json

# Modelo
class Servico:
  def __init__(self, id, descricao, valor, duracao):
    self.__id = id
    self.__descricao = descricao
    if descricao == "": 
      raise ValueError()
    self.__valor = valor
    if valor == "" or valor <= 0: 
      raise ValueError()
    self.__duracao = duracao
    if duracao == "" or duracao <= 0: 
      raise ValueError()

  def set_id(self, c):
    if c != "":
      self.__id = c
    else:
      raise ValueError()

  def get_id(self):
    return self.__id

  def set_descricao(self, c):
    if c != "":
      self.__descricao = c
    else:
      raise ValueError()

  def get_descricao(self):
    return self.__descricao

  def set_valor(self, c):
    if c != "" or c > 0:
      self.__valor = c
    else:
      raise ValueError()

  def get_valor(self):
    return self.__valor

  def set_duracao(self, c):
    if c != "" or c > 0:
      self.__duracao = c
    else:
      raise ValueError()

  def get_duracao(self):
    return self.__duracao

  def __str__(self):
    return f"{self.__id} - {self.__descricao} - R$ {self.__valor:.2f} - {self.__duracao} min"

# Persistência
class Servicos:
  objetos = []    # atributo estático

  @classmethod
  def inserir(self, obj):
    self.abrir()
    m = 0
    for c in self.objetos:
      if c.get_id() > m: 
        m = c.get_id()
    obj.self.__id = m + 1
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
    c = self.listar_id(obj.self.__id)
    if c != None:
      c.self.__descricao = obj.self.__descricao
      c.self.__valor = obj.self.__valor
      c.self.__duracao = obj.self.__duracao
      self.salvar()

  @classmethod
  def excluir(self, obj):
    c = self.listar_id(obj.self.__id)
    if c != None:
      self.objetos.remove(c)
      self.salvar()
  
  @classmethod
  def listar(self):
    self.abrir()
    return self.objetos

  @classmethod
  def salvar(self):
    with open("servicos.json", mode="w") as arquivo:   # w - write
      json.dump(self.objetos, arquivo, default = vars)

  @classmethod
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

