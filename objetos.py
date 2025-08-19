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
print(concatenar)  # Saída: MaxPinheiro

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

