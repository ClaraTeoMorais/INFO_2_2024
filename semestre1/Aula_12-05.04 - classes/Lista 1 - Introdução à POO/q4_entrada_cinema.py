d = input("Digite o dia da sessão de cinema: ")
h = input("Digite o horário da sessão de cinema: ")

class Entrada_Cinema: 
    def __init__(self):
        self.dia = d
        self.hora = int(h)

    def inteira(self):
        if self.dia == "Segunda" or self.dia == "Terça" or self.dia == "Quinta": 
            if self.hora >= 17 and self.hora <=24: 
                ingresso = 16 + (16/2)
                print(f"\nO valor do ingresso é R${ingresso:.2f}")
            else:
                ingresso = 16
                print(f"\nO valor do ingresso é R${ingresso:.2f}")

        
        elif self.dia == "Sexta" or self.dia == "Sábado" or self.dia == "Domingo":
            if self.hora >= 17 and self.hora <=24: 
                ingresso = 20 + (20/2)
                print(f"\nO valor do ingresso é R${ingresso:.2f}")
            else:
                ingresso = 20
                print(f"\nO valor do ingresso é R${ingresso:.2f}")

    def meia(self):
        if self.dia == "Quarta":
            ingresso = 8
            print(f"\nO valor do ingresso é R${ingresso:.2f}")

cinema = Entrada_Cinema()
cinema.inteira()
cinema.meia()