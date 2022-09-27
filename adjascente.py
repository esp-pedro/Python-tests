x = int(input("Digite um número: "))

digit = 1
resto = 1
equaldigit = False
i = 0

while resto != 0 and not equaldigit:
    digit = x % 10
    resto = x // 10
    digit1 = resto % 10
    x = resto
    if digit == digit1:
        equaldigit = True

if equaldigit == True:
    print ("adjascente")
else:
    print ("nope")
    
    