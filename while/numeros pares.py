num = int(input('digite um numero'))

print(num)
quantidade = 0
while True:
    num = num - 1
    if num % 2 == 0:
        print(num)
        quantidade += 1
    elif num <=0:
        print('a quantidade de numeros pares são', quantidade+1)
        break
    