nome = input("Digite um nome:")
escolha= input("Gostou do seu nome? S/N:")

if(escolha=="S"):
    print("Seu nome agora é: {}".format(nome))
elif(escolha=="N"):
    print("O nome {} não foi escolhido".format(nome))
else:
    print("Digite uma alternativa valida")

    