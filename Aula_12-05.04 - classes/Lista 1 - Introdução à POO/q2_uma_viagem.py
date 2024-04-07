d = input("Digite a distência percorrida (em km): ")
t = input("Digite o tempo gasto (em horas): ")

class Viagem:
    def __init__(self):
        self.distancia = float(d)
        self.tempo = float(t)

    def velocidade (self):
        v = self.distancia / self.tempo
        print(f"A velocidade média durante a viagem foi de {v} km/h")

viag = Viagem()
viag.velocidade()