import numpy as np
nomes = []
idades = []
sexos = []

for i in range(4):
    nome = input("Digite o seu nome:").lower()
    nomes.append(nome)
    idade = int(input("Digite a sua idade:"))
    idades.append(idade)
    sexo = input("Digite o seu sexo: F/M:").lower()
    sexos.append(sexo)
    

nome1 = nomes[0]
nome2 = nomes[1]
nome3 = nomes[2]
nome4 = nomes[3]
    
idade1 = int(idades[0])
idade2 = int(idades[1])
idade3 = int(idades[2])
idade4 = int(idades[3])

sexo1 = sexos[0]
sexo2 = sexos[1]
sexo3 = sexos[2]
sexo4 = sexos[3]

pessoas = {nome1 : idade1, nome2 : idade2, nome3 : idade3, nome4 : idade4}
sexope = {nome1 : sexo1, nome2 : sexo2, nome3 : sexo3, nome4 : sexo4}


media = np.mean(idades)
print("A media das idades é: {}".format(media))

if (sexo1 == "f"):
    del pessoas[nome1]   
if (sexo2 == "f"):
    del pessoas[nome2]
if (sexo3 == "f"):
    del pessoas[nome3]
if (sexo4 == "f"):
    del pessoas[nome4]

velho = max(pessoas, key=pessoas.get)
print("O homem mais velho: {}".format(velho))

novas = 0
if (sexo1 == "f" and idade1 < 20):
    novas = novas +1
if (sexo2 == "f" and idade2 < 20):
    novas = novas +1
if (sexo3 == "f" and idade3 < 20):
    novas = novas +1
if (sexo4 == "f" and idade4 < 20):
    novas = novas +1 

print("A quantidade de mulheres mais novas que 20 anos é: {}".format(novas))
 
