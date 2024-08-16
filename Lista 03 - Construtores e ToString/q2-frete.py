class Frete:
    def __init__(self,p,d):
        self.__peso = 0
        self.__distancia = 0
        self.set_peso(p)
        self.set_distancia(d)

    def set_peso(self,v):
        if v >= 0: self.__peso = v
        else: raise ValueError()

    def set_distancia(self,v):
        if v >= 0: self.__distancia = v
        else: raise ValueError()

    def get_peso(self):
        return self.__peso
    
    def get_distancia(self):
        return self.__distancia

    def calc_frete(self):
        return self.__peso * self.__distancia * 0.01

    def __str__(self):
        return (f"\nPeso = {self.__peso} kg / Distância = {self.__distancia} km")

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
        p = float(input("Valor do peso (em kg): "))
        d = float(input("Valor da distância (em km): "))
        f = Frete(p,d)
        print(f)
        print(f"Frete = R${f.calc_frete():.2f}\n")

UI.verif_opc()