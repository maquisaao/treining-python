# LIST COMPREHENSION

x = [1, 2, 3, 4, 5]
y = []

for i in x: # metodo 'simples'
    y.append(i**2)
print(x)
print(y)

# y = [valor_a_adicionar laço condição] *usado list comprehension*
y2 = [i**2 for i in x] # retorna o quadrado da lista x
print(y2)

y3 = [i for i in x if i%2==0] # retorna os pares da lista x
print(y3)

y4 = [i for i in x if i%2==1] # retorna os impares da lista x
print(y4)

# 