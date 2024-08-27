import json
from datetime import datetime

class Paciente:
  def __init__(self,id,n,f,nc):
    self.id = id
    self.nome = n
    self.fone = f
    self.nasc = nc
  def __str__(self):
    return (f"{self.id} - {self.nome} - {self.fone} - {self.nasc}")


class NPaciente:
  pacientes = []  
  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    #calcular o ID
    n = 0
    for i in cls.pacientes:
      if i.id > n: 
        n = i.id
    obj.id = n + 1
    cls.pacientes.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.pacientes
  
  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for i in cls.pacientes:
      if i.id == id: 
        return i
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    i = cls.listar_id(obj.id)
    if i != None:
      i.nome = obj.nome
      i.fone = obj.fone
      i.nasc = obj.nasc
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    i = cls.listar_id(obj.id)
    if i != None:
      cls.pacientes.remove(i)
      cls.salvar()

  @classmethod
  def abrir(cls):
    cls.pacientes = []
    try:
      with open("pacientes.json", mode="r") as arquivo:  
        texto = json.load(arquivo)
        for obj in texto:   
          p = Paciente(obj["id"], obj["nome"], obj["fone"], obj["nasc"])
          cls.pacientes.append(p)
    except FileNotFoundError:
      pass
  
  @classmethod
  def salvar(cls):
    with open("pacientes.json", mode="w") as arquivo: 
      json.dump(cls.pacientes, arquivo, default = vars)

    @classmethod
    def aniversariantes(cls,nc):
        cls.abrir()
        aniversariantes = []
        for nc in aniversariantes:
          if nc.nasc.month == m


class UI:
  @staticmethod
  def menu():
    print("1 - Listar pacientes \n2 - Inserir paciente \n3 - Atualizar paciente \n4 - Excluir paciente \n5- Listar aniversariantes do mês \n6 - Fim")
    return int(input("Escolha uma opção: "))

  @staticmethod
  def main():
    op = 0
    while op != 6:
      op = UI.menu()
      if op == 1: UI.paciente_listar()
      if op == 2: UI.paciente_inserir()
      if op == 3: UI.paciente_atualizar()
      if op == 4: UI.paciente_excluir()
      if op == 5: UI.paciente_aniversariantes()

  @staticmethod
  def paciente_listar():  
    for i in Paciente.listar():
      print(i)

  @staticmethod
  def paciente_inserir():
    nome = input("Digite seu nome: ")
    fone = input("Digite seu telefone: ")
    nasc = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    p = Paciente(0, nome, fone, nasc)
    Paciente.inserir(p)

  @staticmethod
  def paciente_atualizar():
    UI.paciente_listar()
    id = int(input("Informe o id do cliente a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    fone = input("Informe o novo telefone: ")
    nasc = input("Informe a nova data de nascimento (dd/mm/aaaaa): ")
    p = Paciente(id, nome, fone, nasc)
    Paciente.atualizar(p)

  @staticmethod
  def paciente_excluir():
    UI.paciente_listar()
    id = int(input("Informe o id do cliente a ser excluído: "))
    p = Paciente(id, "", "", "")
    Paciente.excluir(p)

    @staticmethod
    def paciente_aniversariantes():
      print("Selecione um mês para ver a lista de aniversariantes (mm): ")
      Paciente.aniversariantes()

UI.main()