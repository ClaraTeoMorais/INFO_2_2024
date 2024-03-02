import math

base,altura = input("Digite a base e a altura do retângulo (respectivamente): ").split()

b = float(base)
h = float(altura)

a = b*h
p = (2*b) + (2*h)
d = math.sqrt((b**2) + (h**2))

print(f"Área = {a:.2f}")
print(f"Perímetro = {p:.2f}")
print(f"Diagonal = {d:.2f}")