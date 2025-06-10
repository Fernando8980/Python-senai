alunos = []

def notas(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    
    
    
    
    
def condicaos(menu):   
    if menu == 1:
        nome_aluno = input("Digite o nome do aluno: ")
        nota1 = int(input("Digite a nota 1: "))
        nota2 = int(input("Digite a nota 2: "))
        nota3 = int(input("Digite a nota 3: "))
        media1 = notas(nota1, nota2, nota3)
        
        alunos.append({
            
            "nome_aluno": nome_aluno,
            "media1": media1
            
            
})    
        cadastro(nome_aluno, nota1, nota2, nota3)
        print("Você cadastrou seu aluno")
        
        
    elif menu == 2:
        print('relatório')
    
    for leitura_relatorio in alunos:
        print("nome do aluno: ",f"{leitura_relatorio['nome_aluno']}")
     

                
def layout():
     print("[1] cadastro")
     print("[2] relatório ")




def cadastro (nome_aluno, nota1, nota2, nota3):
    aluno = {
        "nome_aluno": nome_aluno,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
}
    alunos.append(aluno)
   


while True:
    layout()
    opcao = int(input('digite a opção'))
    condicaos(opcao)

    

       

            
    
    
    
    
    
    
    
    