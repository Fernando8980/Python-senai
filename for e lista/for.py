#1
objetos = ['lapis','estojo','caderno','bolsa','apontador']
#2
objetos.append('borracha')
#3
print(objetos[1])
#4
aleatório = objetos.pop()
print(aleatório)
#5
print(len(objetos))
#6
for objeto in objetos:
    print(objeto)
    
#7
if 'cadeira' in objetos:
    objetos.remove('cadeira')
    print('cadeira removida')
else:
    objetos.append('cadeira')
    print('cadeira adicionada')
#8
print(objetos)
objetos.sort()
print(objetos)
#9
ultimo = objetos[0]
primeiro = objetos [-1]
print('o primeiro item é:', primeiro)
print('o ultimo item é:', ultimo)
#10
objetos.clear()
print('lista vazia')

