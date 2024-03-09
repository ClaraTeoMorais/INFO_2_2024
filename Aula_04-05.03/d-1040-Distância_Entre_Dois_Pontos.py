import math

x1, y1 = input().split()
x2, y2 = input().split()

X1 = float(x1)
X2 = float(x2)
Y1 = float(y1)
Y2 = float(y2)

distancia = math.sqrt( ((X2 - X1)**2) + ((Y2 - Y1)**2) )

print(f"{distancia:.4f}")

