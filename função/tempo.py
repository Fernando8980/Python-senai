velocidade = int(input('digite a velocidade'))
distancia = int(input('digite a distancia'))

def medir_tempo(velocidade, percorrer):
    tempo = distancia / velocidade
    
    print('o percurso levara',tempo,'horas')

print(medir_tempo(velocidade, distancia))