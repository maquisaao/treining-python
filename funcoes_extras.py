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

# FUNCAO ENUMERATE

lista = ["abacate", "bola", "cachorro"]
for i in range(len(lista)): # metodo 'simples' chamar os indices e os itens
    print(i, lista[i])

for i, nome in enumerate(lista): # usando enumerate
    print(i,nome)

# FUNCAO MAP

def dobro(x):
    return x*2

valor = [1, 2, 3, 4, 5]
print (dobro(valor)) # dessa maneira vai acabar duplicando a lista ao invés de dobrar os valores

# map(funcao, lista)

valor_dobrado = map(dobro, valor)
print(valor_dobrado) # printa em formato de objeto 'map' 

valor_dobrado = list(valor_dobrado) # converte em lista ( list )
print(valor_dobrado)

