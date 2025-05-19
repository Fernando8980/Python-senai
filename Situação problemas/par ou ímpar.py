# par ou ímpar
import random

pc = random.randint(1,10)
      

while True :
    print("jogo do Par ou Ìmpar")
    print("vamos jogar?")  
    print("[1]-PAR")
    print("[2]-ÍMPAR")
    print("[3]-OUTRA RODADA")
    print("[0]-SAIR")
    
    escolha = int(input("Faça sua escolha: "))
    if escolha == 0:
        break
    elif escolha == 1:
        print('voce é par eu sou impar')
        num1 = int(input('digite um numero'))
        pc = random.randint(1,10)
        print('aleatorio',pc)
        soma =pc+num1
        if soma % 2 == 0:
            print('voce venceu')
            
        else:
             print('voce perdeu')
        
            
    
    elif escolha ==2:
        print('voce é impar eu sou par ')
        num1 = int(input('digite um numero'))
        print('aleatorio',pc)
        soma = pc+num1
        if soma % 2 == 0:
            print('voce perdeu')
            
        else:
             print('voce venceu')
            
    
        
            
                