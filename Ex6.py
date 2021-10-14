primeiro = int(input("Digite o primeiro numero:"))
razao = int(input("Digite a razao:"))
progressao = 0
for i in range(10):
    progressao = primeiro+(i*razao)
    print(progressao)
