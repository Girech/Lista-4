n1 = int(input("Digite um numero:"))
n2 = int(input("Digite um numero:"))
operacao = input("Escolha uma operacao: * ou /:")

if(operacao=="*"):
    print("O resultado da multiplicação é:", n1*n2)
elif(operacao=="/"):
    print("O resultado da divisão é:", n1/n2)
else:
    print("Escolha uma operação valida")