nome = input("Digite seu nome completo: ")
p = nome.split()
print("Bem vindo(a) ao Python,", p[0])

#SEM USAR O SPLIT

n = nome.index(" ")
prim_nome = nome [0:n]

print("Bem vindo(a) ao Python,", prim_nome)