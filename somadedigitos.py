x = int(input("Digite um número: "))

digit = 1
resto = 1
soma = 0

while resto != 0:
    digit = x % 10
    resto = x // 10
    x = resto
    soma = soma + digit

print(soma)