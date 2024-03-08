x1, y1 = input().split()
x2, y2 = input().split()

X1 = float(x1)
Y1 = float(y1)
X2 = float(x2)
Y2 = float(y2)

Distancia = ((X2 - X1)**2 + (Y2 - Y1)**2) * 0.5

print(f'{Distancia:.4f}')