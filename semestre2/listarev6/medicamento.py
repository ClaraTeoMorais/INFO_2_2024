import json
from datetime import datetime as dt

class Medicamento():
    def __init__(self, id, descricao, valor, vencimento):
        self.id = id
        self.descricao = descricao
        self.valor = valor
        self.vencimento = vencimento

    def __str__(self):
        return f"{self.id} - {self.descricao} - {self.valor} - {self.vencimento.strftime('%d/%m/%Y')}"
    
    def to_json(self):
        dic = []
        dic["id"] = self.id
        dic["descricao"] = self.descricao
        dic["valor"] = self.valor
        dic["vencimento"] = self.vencimento.strftime('%d/%m/%Y')
        return dic
    
    def set_id(self, i):
        if i != "":
            i = self.id
        else: 
            raise ValueError()
        
    def get_id(self):
        return self.id

    def set_descricao(self, d):
        if d != "":
            d = self.descricao
        else: 
            raise ValueError()
        
    def get_descricao(self):
        return self.descricao
    
    def set_valor(self, v):
        if v != "":
            v = self.valor
        else:
            raise ValueError
        
    def get_valor(self):
        return self.valor
    
    def set_vencimento(self, v):
        if v > dt.now():
            v = self.vencimento
        else: raise ValueError("Este medicamento está vencido")
    
    def get_vencimento(self):
        return self.vencimento
    
class Medicamentos():
    medicamentos = []
    
    @classmethod
    def inserir(cls, med):
        cls.abrir()
        n = 0
        for m in cls.medicamentos:
            if m.id > n:
                n = m.id
        med.id = n + 1
        cls.medicamentos.append(med)
        cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.medicamentos
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for m in cls.medicamentos:
            if m.id == id:
                return m
        return None
    
    @classmethod
    def atualizar(cls, med):
        m = cls.listar_id(med)
        if m != None:
            m.descricao = med.descricao
            m.vencimento = med.vencimento
            m.valor = med.valor
            cls.salvar()

    @classmethod
    def excluir(cls, med):
        m = cls.listar_id(med)
        if m.id != None:
            cls.medicamentos.remove(m)
            cls.salvar()
    
    @classmethod
    def abrir(cls):
        cls.medicamentos = []
        try:
            with open('medicamentos.json', mode='r') as arquivo:
                texto = json.load(arquivo)
                for med in texto:
                    c = Medicamento(med["id"], med["descricao"], med["valor"], dt.strptime(["vencimento"], "%d/%m/%Y"))
        except FileNotFoundError:
            pass
    
    @classmethod
    def salvar(cls):
        with open("medicamentos.json", mode="w") as arquivo:
            json.dump(cls.medicamentos, arquivo, default = Medicamento.to_json)

class UI:
    @staticmethod
    def menu():
        print("CADASTRO DE MEDICAMENTOS")
        print("1- Inserir, 2- Listar, 3- Excluir, 4- Atualizar, 5- Fim")
        return int(input("Escolha uma opção: "))

    @staticmethod
    def main():
        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.excluir()
            if op == 4: UI.atualizar()

    @staticmethod
    def inserir():
        descricao = input("Digite a descricao do medicamento")
        valor = input("Digite o valor do medicamento: R$")
        vencimento = dt.strptime(input("Digite a data de vencimento: "), "%d/%m/%Y")
        m = Medicamento(0, descricao, valor, vencimento)
        Medicamentos.inserir(m)

    @staticmethod
    def listar():
        for m in Medicamentos.listar():
            print (m)





