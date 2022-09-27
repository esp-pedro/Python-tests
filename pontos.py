import math

x1 = int(input("Digite o x do primeiro plano: "))
y1 = int(input("Digite o y do primeiro plano: "))
x2 = int(input("Digite o x do segundo plano: "))
y2 = int(input("Digite o y do segundo plano: "))

distancia = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

if distancia >= 10:
    print("longe")
else:
    print("perto")