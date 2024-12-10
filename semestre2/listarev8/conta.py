from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, id, n, c):
        self.id = id
        self.n_conta = int(n)
        self.cliente = c
        self.saldo = 0

    def __str__(self):
        print (f"{self.id} - {self.cliente} - {self.n_conta}")

    def set_cliente(self, c):
        if c != "":
            c = self.cliente
        else: raise ValueError()

    def get_cliente(self):
        return self.cliente
    
    def set_n_conta(self, n):
        if n > 0:
            n = self.n_conta
        else: raise ValueError

    def get_n_conta(self):
        return self.n_conta

    contas = []

    def conta(self, obj):
        n = 0
        for c in self.contas:
            if c.id > n:
                n = c.id
        obj.id = n + 1
        self.contas.append(obj)

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
    @abstractmethod
    def sacar(self):
        pass

    def ver_saldo(self):
        return f"Seu saldo atual é de R${self.saldo:.2f}"

class ContaComum(Conta):
    def __init__(self, n_conta, cliente):
        super().__init__(n_conta, cliente)

    def sacar(self, valor):
        sacar = self.saldo - valor
        if valor > self.saldo:
            raise SaldoError()
        else: 
            return sacar

class ContaEspecial(Conta):
    def __init__(self, n_conta, cliente, limite):
        super().__init__(n_conta, cliente)
        self.limite = limite

    def sacar(self, limite, valor):
        limite = self.limite
        saldo = self.saldo + limite
        sacar = saldo - valor
        if valor > saldo:
            return SaldoError()
        else: return (limite - sacar)

class Poupanca(Conta):
    def __init__(self, n_conta, cliente):
        super().__init__(n_conta, cliente)

    depositos = []

    def depositar(self, valor):
        self.depositos.append(valor)
        super().depositar(valor)
        for x in self.depositos:
            self.saldo += x
        return self.saldo
    
    def sacar(self, valor):
        sacar = self.saldo - valor
        n_depositos = len(self.depositos)
        ultimo_deposito = self.depositos[(n_depositos - 1)] 
        ultimo_deposito -= sacar
        self.depositos.remove([n_depositos - 1])
        self.depositos.append(ultimo_deposito)
        if valor > self.saldo:
            raise SaldoError()
        else: return sacar

class SaldoError(ValueError):
    pass

class UI:
    def menu():
        print("CONTA BANCÁRIA")
        print("1- Criar conta / 2- Conta comum / 3- Conta especial / 4- Saque Poupança / 5- Depósito Poupança / 10- Fim")
        return int(input("Selecione uma das opções"))
    
    def main():
        op = 0
        while op != 10:
            op = UI.menu()
            if op == 1: UI.criar_conta()
            if op == 2: UI.CC()
            if op == 3: UI.CE()
            if op == 4: UI.poupanca_saque()
            if op == 5: UI.poupanca_deposito()

    
    def criar_conta():
        cliente = input("Digite seu nome: ")
        n_conta = int(input("Digite o número da sua conta: "))
        c = Conta(0, n_conta, cliente)
        Conta.conta(c)

    def CC():
        print("SAQUE CONTA COMUM")
        valor = float(input("Digite o valor que você quer sacar: R$"))
        ContaComum.sacar(valor)
        return print(ContaComum.ver_saldo())

    def CE():
        print ("SAQUE CONTA ESPECIAL")
        limite = float(input("Digite seu limite: R$"))
        valor = float(input("Digite o valor que você quer sacar: R$"))
        ContaEspecial.saque(limite, valor)
        return print(ContaEspecial.ver_saldo())

    def poupanca_saque():
        print("SAQUE POUPANÇA")
        valor = float(input("Digite o valor que você quer sacar: R$"))
        Poupanca.sacar(valor)
        return print(Poupanca.ver_saldo())

    def poupanca_deposito():
        print("DEPÓSITO POUPANÇA")
        valor = float(input("Digite o valor que você quer depositar: R$"))
        Poupanca.depositar(valor)
        return print(Poupanca.ver_saldo())
    
UI.main()




        


