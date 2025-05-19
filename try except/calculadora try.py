def calculadora():

    print("=== Calculadora Básica ===")

    while True:

        try:

            # Solicita ao usuário o primeiro número

            num1 = input("Digite o primeiro número (ou 'sair' para encerrar): ")

            if num1.lower() == 'sair':

                print("Calculadora encerrada. Até logo!")

                break

            num1 = float(num1)  # Tenta converter para float

            operador = input("Escolha um operador (+, -, *, /): ")

            num2 = float(input("Digite o segundo número: "))  # Tenta converter para float

            # Executa a operação de acordo com o operador

            if operador == '+':

                resultado = num1 + num2

            elif operador == '-':

                resultado = num1 - num2

            elif operador == '*':

                resultado = num1 * num2

            elif operador == '/':

                if num2 == 0:

                    print("Erro: Divisão por zero não é permitida.")

                    continue

                resultado = num1 / num2

            else:

                print("Operador inválido. Tente novamente.")

                continue

            print(f"O resultado de {num1} {operador} {num2} é: {resultado}")

        except ValueError:

            print("Entrada inválida! Por favor, insira números válidos.")

        except Exception as e:

            print(f"Ocorreu um erro: {e}")
 
# Chama a função da calculadora

calculadora()
 
 
 