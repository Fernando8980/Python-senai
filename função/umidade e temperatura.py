temperatura = int(input('digite a temperatura'))
umidade = int(input('digite a umidade'))

print('')
print('defina estação')
print('[1] inverno')
print('[2] verão')
estaçao = int(input('digite a estação'))


def verificar (temperatura,umidade,estaçao):
    if estaçao == 1:
        print('inverno')
        if temperatura >= 20 and temperatura <= 22 and umidade >= 40 and umidade <= 55:
            print('temperatura e umidade adequada')
        
        elif temperatura >= 20 and temperatura <= 22 and umidade != 40 and umidade != 55:
            print('temperatura é adequada')
            print('umidade inadequada')
        
        elif temperatura != 20 and temperatura != 22 and umidade >= 40 and umidade <= 55:
            print('temperatura é inadequada')
            print('umidade adequada')
        
        elif temperatura != 20 and temperatura != 22 and umidade != 40 and umidade != 55:
            print('temperatura é inadequada')
            print('umidade inadequada')
    if estaçao == 2:
        print('verão')
        if temperatura >= 23 and temperatura <= 26 and umidade >= 40 and umidade <= 65:
            print('temperatura e umidade adequada')
        
        elif temperatura >= 23 and temperatura <= 26 and umidade != 40 and umidade != 65:
            print('temperatura é adequada')
            print('umidade inadequada')
        
        elif temperatura != 23 and temperatura != 26 and umidade >= 40 and umidade <= 65:
            print('temperatura é inadequada')
            print('umidade adequada')
        
        elif temperatura != 23 and temperatura != 26 and umidade != 40 and umidade != 65:
            print('temperatura é inadequada')
            print('umidade inadequada')


verificar(temperatura,umidade,estaçao)
        
        
        
        