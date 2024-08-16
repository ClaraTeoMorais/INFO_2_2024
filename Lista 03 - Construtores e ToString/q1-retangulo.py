class Retangulo:
    def __init__(self,b,h):
        self.__b = 0
        self.__h = 0
        self.set_base(b)
        self.set_altura(h)

    def set_base(self,v):
        if v >= 0: self.__b = v
        else: raise ValueError()

    def set_altura(self,v):
        if v >= 0: self.__h = v
        else: raise ValueError()

    def get_base(self):
        return self.__b
    
    def get_altura(self):
        return self.__h

    def calc_area(self):
        return self.__b * self.__h
    
    def calc_diagonal(self):
        return (((self.__b **2) + (self.__h **2))**(1/2))

    def __str__(self):
        return (f"\nBase = {self.__b} / Altura = {self.__h}")

class UI:
    @staticmethod
    def opc():
        print("1- Calcular / 2- Fim")
        return int(input("Escolha uma das opções: "))
    
    @staticmethod
    def verif_opc():
        opc = 0
        while opc != 2: 
            opc = UI.opc()
            if opc == 1: UI.calcular()

    @staticmethod
    def calcular():
        b = float(input("Valor da base: "))
        h = float(input("Valor da altura: "))
        r = Retangulo(b,h)
        print(r)
        print(f"Área = {r.calc_area():.2f}")
        print(f"Diagonal = {r.calc_diagonal():.2f}\n")

UI.verif_opc()