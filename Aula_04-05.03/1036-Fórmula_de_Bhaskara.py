import math

A, B, C = input ().split()

a = float(A)
b = float(B)
c = float(C)

delta = (b ** 2) - 4 * a * c

if a == 0:
    print ("Impossível calcular")
elif delta < 0:
    print ("Impossível calcular")
else: 
    r1 = (-b + math.sqrt(delta)) / (2 * a)
    r2 = (-b - math.sqrt(delta)) / (2 * a)


print (f"R1 = {r1:.5f}")
print (f"R2 = {r2:.5f}")

# escreva("(-b + ou - raiz(delta)) / (2 * a)\n")
# escreva("(-", b," + ou - raiz(", delta,")) / (2 * ", a,")\n")
# escreva("(", -1 * b," + ou - ", Mat.raiz(delta, 2),") / ", 2 * a,"\n")

# escreva("x1 = ", (-1 * b + Mat.raiz(delta, 2)) / (2 * a),"\n")

# escreva("x2 = ", (-1 * b - Mat.raiz(delta, 2)) / (2 * a),"\n")
# }
# }

