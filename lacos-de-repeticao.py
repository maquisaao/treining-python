# comando while (iteradores)

x = 1 

while x < 10:  
    print(x)
    x = x + 1  # x += 1


x1 = 10
while x1 > 0:
    print(x1)
    x1 -= 1  


x2 = 10
while x % 2 == 0 and x2 > 0:  
    print(x2)
    x2 -= 2

x3 = 2
while x3 % 2 == 0 and x3 <= 10:
    print(x3)
    x3 += 2

# comando for

lista1= [1, 2, 3, 4, 5]
lista2= ['a', 'b', 'c', 'd', 'e']
lista3= ['a', 1, 'b', 2, 'c', True, 10.5]

for i in lista1:
    print(i)
for i in lista2:
    print(i)
for i in lista3:
    print(i)

# comando for com range ( range(inicio, fim, passo) )
for i in range(10): # contagem começa em 0, entao o 10 nao entra
    print(i)

for i in range(10, 20):
    print(i)

for i in range(10, 20, 2): 
    print(i)