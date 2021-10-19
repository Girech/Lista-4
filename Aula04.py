#EXPLICAÇÃO SOBRE LISTAS:

#O QUE É LISTAS?
#É uma lista normal, como uma lista de compras, no pyhton vamos poder listar todas as informações dentro de uma única variável e depois utilizar essas informações dentro do nosso código.

#Uma lista é criada dentro de uma varivel, para criar uma lista é usado o simbolo do colchetes [], e os itens são separados por virgula. 

#criando uma lista, colocando 4 itens na lista:

lista = ['BANANA', 'MAÇA', 'LARANJA', 'MORANGO'] 
print(lista)

#escolhendo itens na lista:
# cada item possiu um "lugar" na lista, uma posição, e essa posição inicia do 0.
print(lista[1])
print(lista[0])
print(lista[2])
print(lista[3], "\n")

#não temos a posição 4 , vamos do 0 ao 3 

#Conseguimos acessar a lista usando número negativos:

print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])

#Adicionando itens na lista:

#Para isso usamos o método .insert() -> Insert é para adicionar em um lugar exato na lista
# e .append() -> Append é para adicionar ao final de uma lista.

lista.append("GOIABA") #adicionel no fim da lista
print(lista)

lista.insert(1,"BOLSA") #adicionei na posição 1 da lista.
print(lista)

#Intervalo de itens:
print(lista[1:3]) 

#Intervalo de itens sem o item de início:
print(lista[:2])

#Intervalo de itens sem o item de final:
print(lista[1:])

#alterando valor de uma lista:
lista[2] =  "MARIANE"



#Removendo itens da lista podemos usar o pop, remove e o del: 

# com o remove temosx)
print(lista)
#ou seja o remove, remove apenas o 1 item com o nome bolsa.


#com o del ele remove o item da lista baseado na sua posição

del lista[0]
print(lista)


#com o pop ele remove o ultimo item da lista, porém não o exclui.
#lista.pop(3) 
#print(lista)

#Se usar o pop sem passar o parâmetro, vai remover o último da lista.
lista.pop()

item = lista.pop(3) 
print(lista)
print(item) #salvei o item removido da lista, e coloquei na variavel item


#criar lista vazia
nova_lista = []
nova_lista.append(item) #adicionei um item a nova lista
print(nova_lista)

#deleta a lista toda APAGA TUDO.
#del lista

#Limpa a lista mas não deleta ela.
lista.clear()
print(lista)

#Inserindo valores novamente
lista.insert(0, "Mariane")
lista.insert(1, "João")
print("Minha lista com novos itens ", lista)

#Copia dados de uma lista para outra lista
lista_copia = lista.copy()
print( lista_copia)

#Adicionando novos valores na nova lista:
lista_copia.append("Carol")
lista_copia.append("Mariane")
print(lista_copia)

# count serve para contar a quantidade de vezes que o item se repete na lista:
print("quantidade de vezes que repete Mariane: ", lista_copia.count("Mariane"))

#juntando as listas: 
lista_nova = lista + lista_copia
print(lista_nova)

#Encontrando a posição de um item na lista
print("Encontrando a posição de um item na lista: ", lista_nova.index("Carol"))


#ordenar a lista em ordem alfabética
print("minha lista ordenada alfabética: ", sorted(lista_copia))

# inverter as posições dos itens
print("minha lista com as posições invertidas ", reversed(lista_copia))


#Verificar se o item está na lista:
if "Mariane" in lista_copia:
    print("Sim, está na lista!")
else:
    print("Não está na lista")
    
    
#lista númerica:

lista_num = [3,6,8,0,2,4,1]
print(lista_num)

#ordenar a lista em ordem numerica:
print("minha lista ordenada numérica: ", sorted(lista_num))

#valor min, max, e soma
min = min(lista_num)
max = max(lista_num)
soma = sum(lista_num)
print (min,max,soma)


#Adicionando item na lista a partir de entrada do usuario.

aluno1 = input("Nome do primeiro aluno: ")
aluno2 = input("Nome do segundo aluno: ")
aluno3 = input("Nome do terceiro aluno: ")
aluno4 = input("Nome do quarto aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]
print(lista)


