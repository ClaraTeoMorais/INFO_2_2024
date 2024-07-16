class Conta():
    def __init__(self):
        self.__nome = ""
        self.__saldo = 0
        self.__n_conta = ""
        self.__valor = 0
    
    def set_nome(self,n):
        if n != "":
            self.__nome = n
        else:
            raise ValueError("Nome inválido")
    
    def get_nome(self):
        return self.__nome

    def set_saldo(self,valor):
        self.__saldo = valor
    
    def get_saldo(self):
        return self.__saldo
    
    def set_n_conta(self,c):
        if c != "":
            self.__n_conta = c
        else:
            raise ValueError("Número da conta inválido")
        
    def get_n_conta(self):
        return self.__n_conta
    
    def set_valor(self,valor):
        self.__valor = valor
    
    def get_valor(self):
        return self.__valor
    
    def saque(self):
        return self.__saldo - self.__valor 
    
    def deposito(self):
        return self.__saldo + self.__valor

class UI():
    @staticmethod
    def inicio(): 
        conta = Conta()
        conta.set_nome(input("Digite seu nome: "))
        conta.set_n_conta(input("Digite o número da sua conta: "))
        conta.set_saldo(float(input("Digite seu saldo: ")))

    @staticmethod
    def opcoes():
        conta = Conta()
        print(f"\n{conta.get_nome()}, digite o número referente a ação que você deseja realizar")
        print("1- Realizar saque")
        print("2- Realizar depósito")
        print("3- Encerrar")
        return (input("Opção: "))
    
    @staticmethod
    def verificar_opc():
        opc = 0
        while opc !=3:
            opc = UI.opcoes()
            if opc == "1":
                UI.final_saque()
            elif opc == "2":
                UI.final_deposito()

    @staticmethod
    def final_saque():
        conta = Conta()
        print(f"Seu saldo atual é de R${conta.get_saldo():.2f}")
        conta.set_valor(float(input("Digite quanto você quer sacar: R$")))
        print(f"O valor a ser sacado é de R${conta.get_valor():.2f}")
        print(f"{conta.get_nome()}, o saldo final da sua conta é de R${conta.saque():.2f}")

    @staticmethod
    def final_deposito():
        conta = Conta()
        print(f"Seu saldo atual é de R${conta.get_saldo():.2f}")
        conta.set_valor(float(input("Digite quanto você quer depositar: R$")))
        print(f"O valor a ser depositado é de R${conta.get_valor():.2f}")
        print(f"{conta.get_nome()}, o saldo final da sua conta é de R${conta.deposito():.2f}")

UI.inicio()
UI.verificar_opc()