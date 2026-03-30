#Solicite ao usuário que informe dois números e depois exiba qual número é maior ou se são iguais.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O primeiro número é maior.")
elif numero2 > numero1:
    print("O segundo número é maior.")
else:
    print("Os dois números são iguais.")
