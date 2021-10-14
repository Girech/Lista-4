idade1 = 0
idade2 = 0
for i in range(7):
    ano = int(input("Digite o seu ano de nascimento:"))
    maior = 2021 - ano
    if (maior>= 18):
        idade1 = idade1 + 1
    else:
        idade2 = idade2 + 1
print("{} pessoas ja são maiores de idade".format(idade1))
print("{} pessoas ainda são menores de idade".format(idade2))