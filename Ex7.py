irmaos = input("Voce possui irmãos? S/N:")

if(irmaos=="S"):
    quantidade = input("quantos irmãos voce tem?")
    print("Voce tem {} irmao(s)".format(quantidade))
elif(irmaos=="N"):
    opniao = input("Gostaria de ter irmaos? S/N:")
    print("Sua resposta foi: {}".format(opniao))
else:
    print("Digite uma resposta valida")