import random

numero = random.randint(0,100)
print(numero) # escolhe aleatoriamente um numero de 0 a 100

lista = [123, 23, 5, 76, 874, 3]
numero = random.choice(lista) # escolhe aleatoriamente um numero de uma lista
print(numero)

# tratamento de exceções

a = 2
b = 0

# se ocorrer um erro dentro do try o programa printa a mensagem do except e mantem rodando o codigo
try:
    print(a/b)
except:
    print("impossivel dividir por zero")

print(a/a)