n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
n3 = float(input("Digite a terceira nota:"))
media = (n1+n2+n3)/2

if(n1<=5 and n2<=5 and n3<=10):
    print("A media do aluno é: {}".format(media))
    if(media>=6):
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")
else: 
    print("Digite notas validas")