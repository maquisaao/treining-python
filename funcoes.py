a=input("Digite um número: ")
b=input("Digite outro número: ")

'''
---definição de função---
def NOME(PARAMETROS):
    COMANDOS

---chamada de função---
NOME(ARGUMENTOS)  
'''

def soma(a,b):
    c= int(a) + int(b)
    print("A soma é:", c) # nesse cado o c é local, e nao vai existir fora do escopo da função
soma(a,b)
print(c)

# refazer o exercicio 5 do exercicios.py usando funções da forma correta ^

def soma(a,b):
    return int(a) + int(b)  

print("A soma é:", soma(a,b)) 

