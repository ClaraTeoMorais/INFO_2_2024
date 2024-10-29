funcionarios = []

a1 = int(input())
funcionarios.append(a1)
a2 = int(input())
funcionarios.append(a2)
a3 = int(input())
funcionarios.append(a3)

testes = []

t1 = (funcionarios[1] * 2) + (funcionarios[2] * 4)

t2 = (funcionarios[0] * 2) + (funcionarios[2] * 2)

t3 = (funcionarios[0] * 4) + (funcionarios[1] * 2)


testes.append(t1)
testes.append(t2)
testes.append(t3)

menor = min(testes)
print(menor)
