triangulo1 = int(input('digite o lado do triangulo'))
triangulo2 = int(input('digite o lado do triangulo'))
triangulo3 = int(input('digite o lado do triangulo'))

if triangulo1 == triangulo2 and triangulo1 == triangulo3 and triangulo3 == triangulo2:      
    print('Triangulo equilatero ')
elif triangulo1 == triangulo2 or  triangulo2 == triangulo3 and triangulo2 != triangulo2 or triangulo2 != triangulo1:
    print('Triangulo isoceles')
elif triangulo1 != triangulo2 and triangulo1 != triangulo2 and triangulo1 != triangulo2:
    print('Triangulo escaleno')

