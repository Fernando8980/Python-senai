def circulo(raio) :
    return 3.14 * (raio * raio)
   
def quadrado(numero1) :
    return numero1 * numero1
   
def retangulo(numero1, numero2) :
    return numero1 * numero2
   
def menu_area():
    print("[1] circulo")
    print("[2] quadrado")
    print("[3] retângulo")
   
    opcao = int(input("ESCOLHA UMA OPÇÃO: "))
   
    if opcao == 1:
        raio = float(input("DIGITE O RAIO DO CIRCULO: "))
        print("área do circulo = ",circulo(raio))
       
    elif opcao == 2 :
        lado = float(input("DIGITE O LADO DO QUADRADO: "))
        print("área do quadrado = ", quadrado(lado))
       
    elif opcao == 3 :
        base = float(input("DIGITE A BASE DO RETÂNGULO: "))
        altura = float(input("DIGITE A ALTURA DO RETÂNGULO: "))
        print("área do retângulo = ", retangulo(base, altura))
       
menu_area()
