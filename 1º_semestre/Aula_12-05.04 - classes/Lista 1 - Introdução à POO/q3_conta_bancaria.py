n = input("Digite seu nome: ")
c = input("Digite o número da sua conta: ")
m = input("Digite seu saldo: ")

print("\nVocê irá ralizar uma ação de depósito ou saque?")
resp = input("Responda 'd' para depósito, e 's' para saque: ")

class Conta:
    def __init__(self):
        self.nome = n
        self.num_conta = float(c)
        self.saldo = float(m)

    def deposito(self):
        if resp == "d":
            valor = float(input("\nQual valor você irá depositar? R$"))
            final = self.saldo + valor
            print(f"\n{self.nome}, o valor do seu saldo final é de R${final:.2f}")

    def saque(self):
        if resp == "s":
            valor = float(input("\nQual valor você irá sacar? R$"))
            final = self.saldo - valor
            print(f"\n{self.nome}, o valor do seu saldo final é de R${final:.2f}")

conta_bancaria = Conta()
conta_bancaria.deposito()
conta_bancaria.saque() 