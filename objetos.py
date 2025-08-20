'''
Objetos possuem atributos(características) e métodos(ações que podem ser aplicadas).
objeto.atributo (verificar o valor do atributo)
objeto.metodo() (executar o método do objeto)
'''
# Strings:

var1 = 1 # atribuindo o valor 1 à variável var1
var2 = '1' # atribuindo o texto '1' à variável var2

a = "Max "
b = "Pinheiro"

concatenar = a + b
print(concatenar)  # Saída: Max Pinheiro

concatenar2 = a + "Silva" + " " + b
print(concatenar2)  # Saída: Max Silva Pinheiro

# funçao len() retorna o tamanho da string

tamanho = len(concatenar)
tamanho2 = len(concatenar2)
print(tamanho)  # Saída: 10
print(tamanho2)  # Saída: 15

# navegar pelo indice da string
print(concatenar2[0])  # Saída: M
print(concatenar2[8])  # Saída: a
print(concatenar2[2])  # Saída: x

print(concatenar2[4:9]) # Saída: Silva

# metodos de string

print(concatenar2)
print(concatenar2.lower())  # converte a string para minúsculas
print(concatenar2.upper())  # converte a string para maiúsculas
print(concatenar2.strip())  # remove espaços no início e no fim

txt = "Plingua Pdo Pp Pagora Ppode Pser Ptraduzida"
print(txt.split("P"))  # divide a string em uma lista de palavras

# busca de substring
print(concatenar2.split()) # divide a string em uma lista de palavras (espaços como delimitadores)
busca = concatenar2.find("Silva") # busca a substring "Silva" e retorna o índice onde começa
print(busca)  # Saída: 4 (índice onde "Silva" começa)
print(concatenar.find("Silva")) # Saída: -1 (não encontrado)  
print(concatenar2[busca:])  # Saída: Silva Pinheiro (substitui o texto encontrado por "Silva Pinheiro")

# substituição de substring
print(concatenar2.replace("Silva", "Wilson")) # substitui "Silva" por "Wilson"