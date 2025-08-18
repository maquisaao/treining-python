# if

''' if CONDICAO
    EXECUTE_ESSA_LINHA''' 

a=2
b=1

if a < b:
    print("a é menor que b")   
if a > b:
    print("a é maior que b")

# if e else
''' if CONDICAO
    EXECUTE_ESSA_LINHA
else
    EXECUTE_ESSA_LINHA '''

a1=1
b1=2

if a1 < b1:
    print("a1 que b1")        
else:
    print("a1 não é menor que b1")    

# elif
''' if CONDICAO
    EXECUTE_ESSA_LINHA  
elif CONDICAO
    EXECUTE_ESSA_LINHA
else
    EXECUTE_ESSA_LINHA '''

a2=8
b2=7

if a2 > b2:
    print("a2 é maior que b2") #executa o primeir verdadeiro
elif a2 > 0: 
    print("a2 é positivo")

