class viagem():
    def __init__(self):
        self.__d = 1
        self.__t = 1

    def set_distancia(valor,self):
        if valor > 0: 
            self.__d = valor
        else:
            raise ValueError ("A distância não pode ser negativa")
        
    def get_distancia(self):
        return self.__d
    
    def set_tempo(valor,self):
        if valor > 0:
            self.__t = valor
        else: 
            raise ValueError ("O tempo não pode ser negativo")
    
    def get_tempo(self):
        return self.__t

    def velocidade_media(self):
        return self.__d / self.__t
    

class UI():
    
    @staticmethod
    def opcoes():
        print("1- Calcular a velocidade média")
        print("2- Encerrar")
        return (int(input("Escolha uma das opções: ")))

    @staticmethod
    def verificar_opc():
        opc = 0
        while opc != 2:
            opc = UI.opcoes()
            if opc == 1:
                UI.v()

    @staticmethod
    def v():
        velocidade = viagem()
        velocidade.set_distancia(float(input("Digite a distância percorrida (em km): ")))
        velocidade.set_tempo(float(input("Digite o tempo que a viagem durou(em horas): ")))
        print(f"A diatância é = {velocidade.get_distancia()} km")
        print(f"O tempo é = {velocidade.get_tempo()}h")
        print(f"\nVelocidade Média = {velocidade.velocidade_media():.2f}km/h")

UI.verificar_opc()