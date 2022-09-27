x = int(input("Digite um número: "))

digit = x % 10
resto = x // 10
digit1 = resto % 10
resto1 = resto // 10
digit2 = resto1 % 10
soma = digit + digit1 + digit2
print(digit)
print(resto)
print(digit1)
print(resto1)
print(digit2)
print(soma)
