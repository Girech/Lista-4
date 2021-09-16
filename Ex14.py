sexo = input("Digite a inicial do seu sexo, F-Feminino e M-Masculino:")
altura = float(input("Digite a sua altura:"))

if(sexo=="F"):
    print("O seu peso ideal é:",(72.7 * altura) - 58 )
elif(sexo=="M"):
    print("O seu peso ideal é:",(62, 1 * altura) - 44, 7)
else:
    print("Escolha uma alternativa valida")