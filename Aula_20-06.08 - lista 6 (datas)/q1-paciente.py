from datetime import datetime

class Paciente:
    def __init__(self,n,c,t,nasc):
        self.__n = n
        self.__c = c
        self.__t = t
        self.__nasc = nasc

    def set_nome(self,n)
        if n != "":
            self.__n = n
        else: raise ValueError()

    def set_cpf(self,c)
        if c != "":
            self.__c = c
        else: raise ValueError()

    def set_tel(self,t)
        if t != "":
            self.__t = t
        else: raise ValueError()

    def set_nasc(self,nasc)
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
        print(f"{self.__n}, {self.__c}, {self.__t}, {self.__nasc}")

class UI:
    
    

