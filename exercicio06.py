#Faça uma calculadora simples contendo as operações: soma, subtração, divisão e multiplicação. 
#Solicite ao usuário que informe dois número e que informe também a operação que deseja realizar (+, -, /, *) e depois exiba o resultado.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação (+, -, /, *): ")

if operacao == "+":
    resultado = num1 + num2
    print("Resultado:", resultado)

elif operacao == "-":
    resultado = num1 - num2
    print("Resultado:", resultado)

elif operacao == "*":
    resultado = num1 * num2
    print("Resultado:", resultado)

elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("Erro: divisão por zero.")

else:
    print("Operação inválida.")
