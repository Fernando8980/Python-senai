nascimento = int(input('digite um ano'))
ano = 2025
idade = ano-nascimento
if idade<=10:
    print('é criança')
elif idade >=11 and idade <=17:
    print('é adolescente')
elif idade >=18 and idade <=59:
    print('é adulto')
elif idade >=60 and idade <=115:
    print('é idoso')
else:
    print('erro')
