temp = int(input("Digite a temperatura atual:"))

if(temp>25):
    print("O clima está quente")
elif(temp>=18 and temp<=25):
    print("O clima está agradavel")
elif(temp<18):
    print("O clima está frio")