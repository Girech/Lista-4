for i in range(5):
    numero = int(input("Digite um numero:"))
    if (numero%numero==0 and numero%2!=0 and numero%3!=0):
        print("{} é um numero primo".format(numero))
    elif(numero==2 or numero==3):
         print("{} é um numero primo".format(numero))
    else:
        print("{} Não é um numero primo".format(numero))