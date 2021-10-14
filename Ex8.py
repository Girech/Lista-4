for i in range(5):
    palavra = str(input("Digite a frase/palavra:"))
    invertida = palavra[::-1]
    if(palavra == invertida):
        print("A frase é um palíndromo")
    else:
        print("A frase nao é um palíndromo")
