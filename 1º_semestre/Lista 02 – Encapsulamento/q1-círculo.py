class Circulo():
    def __init__(self):
        self.__r = 0

    def set_raio(self,valor):
        if valor > 0:
            self.__r = valor
        else: 
            raise ValueError ("O valor do raio não pode ser negativo")

    def get_raio(self):
        return self.__r
    
    def calc_area(self):
        return 3.14 * self.__r ** 2

class UI:

    @staticmethod
    def menu():
        print("1- Calcular área e comprimento da cirfunferência")
        print("2- Encerrar")
        return int(input("Escolha uma opção: "))

    @staticmethod
    def area_circunferencia():
        c = Circulo()
        c.set_raio(float(input("Digite o valor do raio: ")))
        print(f"A circunferência tem raio = {c.get_raio()}cm")
        print(f"\nÁrea = {c.calc_area():.2f}cm")

    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = UI.menu()
            if op == 1: 
                UI.area_circunferencia()

UI.main()