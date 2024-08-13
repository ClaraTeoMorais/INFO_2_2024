import enum

# Quando for enum IntFlag precisa ser de potência de base dois
class Dia(enum.IntFlag): 
    Domingo = 1    # 0000.0001
    Segunda = 2    # 0000.0010
    Terça = 4      # 0000.0100
    Quarta = 8     # 0000.1000
    Quinta = 16    # 0001.0000
    Sexta = 32     # 0010.0000
    Sábado = 64    # 0100.0000

hoje = Dia.Terça
peoo = Dia.Terça | Dia.Sexta # | significa "e"
fds = Dia.Sábado | Dia.Domingo

print(hoje)
print(peoo)

# quando for um "ou" basta ter 1 e 1 que o resultado será 1 (1 e 1) -> números binários