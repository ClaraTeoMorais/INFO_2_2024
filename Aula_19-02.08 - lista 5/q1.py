class Jogador:
    def __init__(self, nome, camisa, gols):
        self.__nome = ""
        self.__camisa = ""
        self.__gols = ""

    def set_nome(self,x):
        if x != "": self.__nome = x
        else: raise ValueError("Digite um nome")

    def set_camisa(self,x):
        if x != "": self.__nome = x
        else: raise ValueError("Digite o número da camisa")

    def set_gols(self,x):
        if x >= 0: self.__nome = x
        else: raise ValueError("Valor inválido")
    
    def get_nome(self):
        return self.__nome
    
    def get_camisa(self):
        return self.camisa
    
    def get_gols(self):
        return self.__gols
    
    def __str__(self):
        print(f"Nome: {self.__nome} / Camisa: {self.camisa} / Gols: {self.__gols}")

class Time:
    def __init__(self, nome, estado):
        self.__nome = ""
        self.__estado = ""
        self.__jogadores = []

    def set_nome(self,x):
        if x != "": self.__nome = x
        else: raise ValueError("Digite um nome")

    def set_estado(self,x):
        if x != "": self.__nome = x
        else: raise ValueError("Digite o nome do Estado")

    def get_nome(self):
        return self.__nome
    
    def get_camisa(self):
        return self.camisa

    


