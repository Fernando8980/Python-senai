def calcular(peso, distancia, taxa_fixa):
    valor = (peso * 0.5) + (distancia * 0.1) + taxa_fixa
    print('o valor do frete será de', valor, 'reais')

peso = int(input('digite o peso da compra '))
distancia = int(input('digite a distancia'))
taxa_fixa = int(input('digite a taxa'))

calcular(peso, distancia, taxa_fixa)