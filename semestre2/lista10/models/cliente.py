import json

# Modelo
class Cliente:
  def __init__(self, id, nome, email, fone, senha):
    self.__id = id
    if id == "": 
      raise ValueError()
    self.__nome = nome
    if nome == "": 
      raise ValueError("O nome não pode ser vazio")
    self.__email = email
    if email == "": 
      raise ValueError("O email não pode ser vazio")
    self.__fone = fone
    if fone == "": 
      raise ValueError("O telefone não pode ser vazio")
    self.__senha = senha
    if senha == "": 
      raise ValueError("A senha não pode ser vazia")

  def set_id(self, c):
    if c != "":
      self.__id = c
    else:
      raise ValueError()

  def get_id(self):
    return self.__id

  def set_nome(self, c):
    if c != "":
      self.__nome = c
    else:
      raise ValueError("O nome não pode ser vazio")

  def get_nome(self):
    return self.__nome

  def set_email(self, c):
    if c != "":
      self.__email = c
    else:
      raise ValueError("O email não pode ser vazio")

  def get_email(self):
    return self.__email

  def set_fone(self, c):
    if c != "":
      self.__fone = c
    else:
      raise ValueError("O telefone não pode ser vazio")

  def get_fone(self):
    return self.__fone

  def set_senha(self, c):
    if c != "":
      self.__senha = c
    else:
      raise ValueError("A senha não pode ser vazia")

  def get_senha(self):
    return self.__senha

  def __str__(self):
    return f"{self.__nome} - {self.__email} - {self.__fone}"

# Persistência
class Clientes:
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
      c.self.__nome = obj.self.__nome
      c.self.__email = obj.self.__email
      c.self.__fone = obj.self.__fone
      c.self.__senha = obj.self.__senha
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
    self.objetos.sort(key=lambda cliente: cliente.get_nome())
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
          c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"])
          self.objetos.append(c)
    except FileNotFoundError:
      pass

