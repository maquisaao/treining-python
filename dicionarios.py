'''
Em Python, dicionarios sao arrays* associativos. ou seja, um determinado valor passa a ser vinculado a uma chave. Exemplo:
*array é uma estrutura de dados que armazena uma coleçao de elementos, todos do mesmo tipo.
'''
dicionarios_sites = {"Max":"max.com.br"}

# No dicionario acima, a chave "Max" foi vinculada ao valor "max.com.br". Assim, para imprimir o valor chame:

print(dicionarios_sites["Max"])
# será impresso "max.com.br"

# Se o dicionario tiver varios elementos, pode-se usar laços para imprimi-los:
dicionario2 = {"Max":"max.com.br", "Google":"google.com", "Udemy":"udemy.com"}

for chave in dicionario2:
    print([chave]) 

for chave in dicionario2:
    print([dicionario2])

for chave in dicionario2.items(): # essas funcoes (items/values/keys retornam tuplas(imutaveis))
    print([chave])

for chave in dicionario2.values():
    print([chave])

for chave in dicionario2.keys():
    print([chave])
