class Equacao:
    def __init__(self,a,b,c):
        self.__a = 0
        self.__b = 0
        self.__c = 0
        self.__delta = 0
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)

    def set_a(self,v):
        if v != 0: self.__a = v
        else: raise ValueError()

    def set_b(self,v):
        self.__b = v

    def set_c(self,v):
        self.__c = v

    def get_a(self):
        return self.__a
    
    def get_b(self):
        return self.__b
    
    def get_c(self):
        return self.__c

    def delta(self):
        self.__delta = ((self.__b ** 2) - (4 * self.__a * self.__c))
        return self.__delta
    
    def tem_raizes_reais(self):
        if self.__delta >= 0: return True
    
    def raiz_1(self):
        return ( -self.__b + (self.__delta**(1/2)) ) / (2 * self.__a)
    
    def raiz_2(self):
        return ( -self.__b - (self.__delta**(1/2)) ) / (2 * self.__a)

    def __str__(self):
        return (f"\nf(x) = ({self.__a})x² + ({self.__b})x + ({self.__c})")

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
        a = float(input("\nDigite o valor de 'a': "))
        b = float(input("Digite o valor de 'b': "))
        c = float(input("Digite o valor de 'c': "))
        e = Equacao(a,b,c)
        print(e)
        print(f"\nRaiz 1 = {e.raiz_1():.2f}")
        print(f"Raiz 2 = {e.raiz_2():.2f}\n")

UI.verif_opc()