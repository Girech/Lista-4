contador = 1
n = {}
elementos = []
s = 0
while contador != 7:
    nv = 1
    n[nv]= int(input("Digite um elemento:"))
    elementos.append(n[nv]) 
    nv += 1
    contador = contador+1   
for i in elementos:
    if(i%2==0):
        s += i
print(s)




