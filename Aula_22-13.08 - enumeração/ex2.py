import enum

# não se usa IntFlag porque não está somando os valores

class Estado_Mensagem(enum.Enum):
    Enviando = 1
    Enviada = 2
    Recebida = 3
    Lida = 4

class Mensagem:
    def __init__(self,texto):
        self.texto = texto 
        self.estado = Estado_Mensagem.Enviando

