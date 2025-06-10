numero = int(input('digite um numero  '))

def verificar_positivo(numero):
    
    if numero >=1:
        return True
    elif numero <= 1:
        return False
print(verificar_positivo(numero))