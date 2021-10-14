contador = 1
n = {}
elementos = []
s = 0
for i in range (5):
    nv = 1
    n[nv]= float(input("Digite o seu peso:"))
    elementos.append(n[nv]) 
    nv += 1
    contador = contador+1   
elementos.sort(reverse=True)
print(elementos)   
print(elementos[0])
print(elementos[4])