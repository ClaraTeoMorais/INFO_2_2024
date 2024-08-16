from datetime import datetime

class Paciente:
    def __init__(self,n,c,t,nasc):
        self.__n = n
        self.set_nome(n)
        self.__c = c
        self.set_cpf(c)
        self.__t = t
        self.set_tel(t)
        self.__nasc = nasc
        self.set_nasc(nasc)

    def set_nome(self,n):
        if n != "":
            self.__n = n
        else: raise ValueError()

    def set_cpf(self,c):
        if c != "":
            self.__c = c
        else: raise ValueError()

    def set_tel(self,t):
        if t != "":
            self.__t = t
        else: raise ValueError()

    def set_nasc(self,nasc):
        if nasc < datetime.now():
            self.__nasc = nasc
        else: raise ValueError("Data inválida")

    def get_nome(self):
        return self.__n

    def get_cpf(self):
        return self.__c

    def get_tel(self):
        return self.__t

    def get_nasc(self):
        return self.__nasc

    def idade(self):
        return self.__nasc - datetime.now()
    
    def __str__(self):
        return print(f"\nNome: {self.__n}\nCPF: {self.__c}\nTelefone{self.__t}\nData de nascimento: {self.__nasc}")

class UI:
    @staticmethod
    def opcoes():
        print("1- Cadastrar paciente")
        print("2- Encerrar")
        return (int(input("Escolha uma das opções: ")))

    @staticmethod
    def verificar_opc():
        opc = 0
        while opc != 2:
            opc = UI.opcoes()
            if opc == 1:
                UI.p()

    @staticmethod
    def p():
        n = input("Digite seu nome: ")
        c = input("Digite seu CPF: ")
        t = input("Digite seu telefone: ")
        nasc = input("Digite sua data de nascimento (dd/mm/aaaa): ")
        nasc = datetime.strptime(nasc, "%d/%m/%Y")
        p = Paciente(n,c,t,nasc)
        print(p)
        print(f"Idade: {p.idade()}")

UI.verificar_opc()