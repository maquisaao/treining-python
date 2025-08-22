import math

# 1 Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.   
idade = int(input("Digite sua idade:"))
if idade < 18:
    print("Menor de idade")
else:
    print("Maior de idade")


# 2 Faça um programa que receba duas notas digitadas pelo usuário.  
# Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado. 

nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
media= (nota1 + nota2) / 2
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")


# 3 Escreva um programa que resolva uma equação de segundo grau. 
a = int(input("Valor de a:"))
b = int(input("Valor de b:"))
c = int(input("Valor de c:"))

delta = int((b**2)-(4*a*c))

if delta <0:
        print("Raiz de numero negativo.")
else:

    print("Delta é:", delta)
    raiz_de_delta = int(math.sqrt(delta))
    raiz1 = ((b*-1)+(raiz_de_delta))/2
    raiz2 = ((b*-1)-(raiz_de_delta))/2
    print("As raizes da equação são:", raiz1, raiz2)

# 4 Escreva um programa que ordene uma lista numérica com três elementos.
lista = [32, 58, 2]

lista.sort()
print(lista)

# 5 Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal (CALCULADORA)


a = int(input(""))
sinal = input("")
b = int(input(""))


if sinal == "+":
    def soma(a,b):
        resultado = a+b
        print(resultado)
    soma(a,b)
elif sinal == "-":
    def subtracao(a,b):
        resultado = a-b
        print(resultado)
    subtracao(a,b)
elif sinal == "*":
    def multiplicacao(a,b):
        resultado = a-b
        print(resultado)
    multiplicacao(a,b)
elif sinal == "/":
    def divisao(a,b):
        resultado = a-b
        print(resultado)
    divisao(a,b)
else:
    print("Verifique o sinal e tente de novo.")

