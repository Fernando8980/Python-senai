nota1 = int(input("solicite uma nota"))
nota2 = int(input('solicite outra nota'))
soma = nota1+nota2
média = soma/2
if média >=70:
    print('aprovado')
elif média >=50 and 70:
    print('recuperação')
elif média <=50:
    print('reprovado')