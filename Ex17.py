idade = int(input("Digite a sua idade:"))
tempo = int(input("Digite o seu tempo de contribuição:"))

if(idade >=65 or tempo>=30 or (idade>=60 and tempo>=25)):
    print("Voce pode se aposentar")
else:
    print("Voce não pode se aposentar")