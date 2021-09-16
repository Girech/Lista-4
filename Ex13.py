escolha = int(input("A temperatura vai ser convertida de 1)Fº->Cº ou de 2)Cº->Fº?"))
temp = float(input("Digite a temperatura a ser convertida:"))

if(escolha==1):
    print("A temperatura em Cº é de:",(temp * 9/5) + 32)
elif(escolha==2):
    print("A temperatura em Fº é de:", (temp - 32) * 5/9)
else:
    print("Digite um valor valido")