import json
from datetime import datetime

class Paciente:
  def __init__(self, id, n, f, da):
    self.id = id
    self.nome = n 
    self.fone = f
    self.nasc = da
  def __str__(self):
    return f"{self.id} - {self.nome} - {self.fone} - {self.nasc}"
  def to_json(self):
    dic = {}
    dic["id"] = self.id
    dic["nome"] = self.nome
    dic["fone"] = self.fone
    dic["nasc"] = datetime.strftime(self.nasc, "%d/%m/%Y")

    return(dic)

class NPaciente:
  pacientes = []
  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    #calcular ID
    m = 0
    for p in cls.pacientes:
      if p.id > m: 
        m = p.id
    obj.id = m + 1
    cls.pacientes.append(obj)
    cls.salvar()

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for p in cls.pacientes:
      if p.id == id: 
        return p
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    h = cls.listar_id(obj.id)
    if h != None:
      h.nome = obj.nome
      h.fone = obj.fone
      h.nasc = obj.nasc
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    p = cls.listar_id(obj.id)
    if p != None:
      cls.pacientes.remove(p)
    cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.pacientes
  
  @classmethod
  def salvar(cls):
    with open("pacientes.json", mode="w") as arquivo:
      json.dump(cls.pacientes, arquivo, default = Paciente.to_json)

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

  def aniversariantes(cls, obj):
    cls.abrir()
    aniversariantes = []
    for p in cls.pacientes:
        if p.nasc.month == obj:
            aniversariantes.append(p)
        else:
            pass
    if len(aniversariantes) != 0:
        pass
    else: 
        aniversariantes.append("Não há aniversariantes no mês. ")
    return aniversariantes

class UI:
  @staticmethod
  def menu():
    print("1 - Inserir paciente \n2 - Listar paciente \n3 - atualizar paciente \n4 - excluir paciente \n5 - listar aniversariantes do mês \n6 - fim")
    return int(input("Escolha uma opção: "))

  @staticmethod
  def main():
    op = 0
    while op != 6:
      op = UI.menu()
      if op == 1: UI.paciente_inserir()
      if op == 2: UI.paciente_listar()
      if op == 3: UI.paciente_atualizar()
      if op == 4: UI.paciente_excluir()
      if op == 5: UI.aniversariantes()

  @staticmethod
  def paciente_inserir():
    #id = int(input("Informe o id: "))
    nome = input("Informe o nome: ")
    fone = input("Informe o telefone: ")
    nasc = input("Informe a data de nascimento (dd/mm/aaaa): ")
    nasc = datetime.strptime(nasc, "%d/%m/%Y")
    p = Paciente(0, nome, fone, nasc)
    NPaciente.inserir(p)

  @staticmethod
  def paciente_listar():  
    for p in NPaciente.listar():
      print(p)

  @staticmethod
  def paciente_atualizar():
    UI.paciente_listar()
    id = int(input("Informe o id do paciente a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    fone = input("Informe o novo telefone: ")
    nasc = input("Informe a nova data de nascimento (dd/mm/aaaa): ")
    nasc = datetime.strptime(nasc, "%d/%m/%Y")
    p = Paciente(id, nome, fone, nasc)
    NPaciente.atualizar(p)

  @staticmethod
  def paciente_excluir():
    UI.paciente_listar()
    id = int(input("Informe o id do paciente a ser excluído: "))
    p = Paciente(id, "", "", "")
    NPaciente.excluir(p)

  @staticmethod
  def aniversariantes():
    mes = int(input("Escolha um mês para ver a lista de aniversariantes (mm): "))
    a = NPaciente.aniversariantes(NPaciente, mes)
    for x in a:
      print(x)

UI.main()