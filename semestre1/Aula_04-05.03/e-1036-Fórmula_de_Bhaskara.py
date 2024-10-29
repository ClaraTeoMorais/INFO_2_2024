import math

A, B, C = input ().split()

a = float(A)
b = float(B)
c = float(C)

delta = (b ** 2) - 4 * a * c

if a == 0:
    print ("Impossivel calcular")
elif delta < 0:
    print ("Impossivel calcular")
else: 
    r1 = (-b + math.sqrt(delta)) / (2 * a)
    r2 = (-b - math.sqrt(delta)) / (2 * a)

    print (f"R1 = {r1:.5f}")
    print (f"R2 = {r2:.5f}")





