import json
from datetime import datetime

class Jogo:
    def __init__(self, id, n, e, d):
        self.id = id
        self.nome = n
        self.empresa = e
        self.data = d

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.empresa} - {self.data.strftime('%d/%m/%Y')}"
    
    def to_json(self):
      dic = {}
      dic["id"] = self.id
      dic["nome"] = self.nome
      dic["empresa"] = self.empresa
      dic["data"] = self.data.strftime("%d/%m/%Y")
      return dic    

class Jogos:
  objetos = [] 

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    n = 0
    for j in cls.objetos:
      if j.id > n: 
        n = j.id
    obj.id = n + 1
    cls.objetos.append(obj)
    cls.salvar()
      
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for j in cls.objetos:
      if j.id == id: 
        return j
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    j = cls.listar_id(obj.id)
    if j != None:
      j.nome = obj.nome
      j.empresa = obj.empresa
      j.data = obj.data
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    j = cls.listar_id(obj.id)
    if j != None:
      cls.objetos.remove(j)
      cls.salvar()
    
  @classmethod
  def maisNovos(cls):
    cls.abrir()
    nova_lista = []
    nova_lista = sorted(cls.objetos, key=lambda x: x.data)
    return nova_lista

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("jogos.json", mode="r") as arquivo: 
        texto = json.load(arquivo)
        for obj in texto:   
          c = Jogo(obj["id"], obj["nome"], obj["empresa"], datetime.strptime(obj["data"], "%d/%m/%Y"))
          cls.objetos.append(c)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("jogos.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default = Jogo.to_json)

class UI:
  @staticmethod
  def menu():
    print("\nCADASTRO DE JOGOS")
    print("  1 - Inserir\n  2 - Listar\n  3 - Atualizar\n  4 - Excluir\n  5 - Listar por data de lançamento")
    print("Outras opções")
    print("  9 - Fim")
    return int(input("Informe uma opção: "))

  @staticmethod
  def main():
    op = 0
    while op != 9:
      op = UI.menu()
      if op == 1: UI.jogo_inserir()
      if op == 2: UI.jogo_listar()
      if op == 3: UI.jogo_atualizar()
      if op == 4: UI.jogo_excluir()
      if op == 5: UI.jogo_maisNovos()

  @staticmethod
  def jogo_inserir():
    nome = input("\nInforme o nome do jogo: ")
    empresa = input("Informe o nome da espresa: ")
    data = datetime.strptime(input("Informe a data de lançamento (dd/mm/aaaa): "), "%d/%m/%Y")
    j = Jogo(0, nome, empresa, data)
    Jogos.inserir(j)

  @staticmethod
  def jogo_listar():  
    for j in Jogos.listar():
      print(j)

  @staticmethod
  def jogo_maisNovos():  
    for j in Jogos.maisNovos():
      print(j)

  @staticmethod
  def jogo_atualizar():
    UI.jogo_listar()
    id = int(input("\nInforme o id do jogo a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    empresa = input("Informe a nova empresa: ")
    data = datetime.strptime(input("Informe a nova data de lançamento (dd/mm/aaaa): "), "%d/%m/%Y")
    j = Jogo(id, nome, empresa, data)
    Jogos.atualizar(j)
  
  @staticmethod
  def jogo_excluir():
    UI.jogo_listar()
    id = int(input("\nInforme o id do jogo a ser excluído: "))
    j = Jogo(id, "", "", "")
    Jogos.excluir(j)

 
UI.main()