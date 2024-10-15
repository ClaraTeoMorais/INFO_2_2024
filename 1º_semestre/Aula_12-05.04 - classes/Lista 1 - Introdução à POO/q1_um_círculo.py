raio = input("Digite o raio da cirfunferência: ")

class Circulo:
    def __init__(self): # "INIT" -> contrutor / permite criar a funcionalidade inicial da classe
        # SELF -> serve para acessar os métodos e as propriedades de uma instância
        # INSTÂNCIA -> obj cujo comportamento e estado são definidos pela classe
        
        self.raio = float(raio)
    
    def area(self):
        area = 3.14 * self.raio * self.raio
        print(f"Área: {area}")

    def comprimento(self):
        comprimento = 2 * 3.14 * self.raio
        print(f"Comprimento circunferência: {comprimento}")

circunf = Circulo()
circunf.area()
circunf.comprimento()
