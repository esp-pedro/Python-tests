import math

a = float(input("Qual o valor de a? "))
b = float(input("Qual o valor de b? "))
c = float(input("Qual o valor de c? "))

delta = (b ** 2) - 4 * a * c

if delta == 0:
    raiz =  ((-(b)) + math.sqrt(delta)) / (2 * a)
    print("a raiz desta equação é", raiz)
else:
    if delta > 0:
            raiz =  (-b + math.sqrt(delta)) / (2 * a)
            raiz2 =  (-b - math.sqrt(delta)) / (2 * a)
            if raiz2 >= raiz:
                print("as raízes da equação são", raiz, "e", raiz2)
            else:
                print("as raízes da equação são", raiz2, "e", raiz)
    else:
            print("esta equação não possui raízes reais")

           