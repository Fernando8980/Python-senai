
#-----------dicionários-----------

#criar
aluno = {
   'nome':'fer',
   'idade':16,
   'altura':1.78,
   'matriculado':True 
}
celular = {
    'nome':'galaxy s24',
    'marca':'samsug',
    'preço':2699,
    
}    
celular2 = {
    'nome':'iphone 16',
    'marca':'apple',
    'preço':5309,

}
celular3 = {
    'nome':'moto g55',
    'marca':'motorola',
    'preço':1352,

}
#print(celular)

#adicionar campo
aluno['peso'] = 65

#print(aluno)

#alterar campo
aluno['idade'] = 17
#print(aluno)

#deletar campo
del aluno ['altura']
print(aluno)

#verificar
if 'altura' in aluno:
    print('altura existente')
else:
    print('altura inexistente')

#exibir

for chave, valor in aluno.items():
    print(f'{chave}: {valor}')
    
#exibir uma lista de dicionarios
lista_celular = [celular, celular2, celular3]

    #escolhendo os campos
for celular in lista_celular:
    print(f"{celular['nome']}")
    
    #exibindo todos
for celular in lista_celular:
    for chave, valor in celular.items():
        print(f'{chave} - {valor}')
    print()


    

    
    



