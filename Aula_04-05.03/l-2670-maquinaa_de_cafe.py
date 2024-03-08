funcionarios = []

a1 = int(input())
funcionarios.append(a1)
a2 = int(input())
funcionarios.append(a2)
a3 = int(input())
funcionarios.append(a3)

maior = max(funcionarios)
posicao_maior = funcionarios.index(maior)

if posicao_maior == 0:
    p1 = funcionarios[1] * 2
    p2 = funcionarios[2] * 4
    total = p1 + p2
    print(total)

elif posicao_maior == 1:
    p0 = funcionarios[0] * 2
    p2 = funcionarios[2] * 2
    total = p0 + p2
    print(total)

elif posicao_maior == 2:
    p0 = funcionarios[0] * 4
    p1 = funcionarios[1] * 2
    total = p0 + p1
    print(total)