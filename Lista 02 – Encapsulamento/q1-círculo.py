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