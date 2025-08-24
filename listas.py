minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista_2 = [1,2,3,4,5]
minha_lista_3 = ["abacaxi", 2, 9.89, True]
minha_lista_4 = []

# indices começam em 0

print(minha_lista[0])
print(minha_lista[1])
print(minha_lista[2])

# listar usando for
for item in minha_lista_3:
    print (item)

# verificar tamanho de uma lista
tamanho = len(minha_lista)
print(tamanho)

# adicionar elementos a lista
minha_lista_4.append("banana")
minha_lista_4.append("pirulito")
minha_lista_4.append(1)
minha_lista_4.append(False)

print(minha_lista_4)

# verificar se um elemento pertence a uma lista
busca = "picole"
if busca in minha_lista_4:
    print("Tem pirulito nessa lista.")
else:
    print("Nao tem pirulito nessa lista")

# remover elementos de uma lista
del minha_lista_3[2:] #usar [:] pra remover tudo
print(minha_lista_3)

# ordenar uma lista
minha_lista.sort()
print(minha_lista)

minha_lista.sort(reverse=True) # inverte a ordem da lista
minha_lista.reverse() # reverte os valores (o ultimo passa a ser o primeiro e etc)

lista_ordenada = minha_lista.sorted() # retorna uma lista ordenada e exige uma variavel

