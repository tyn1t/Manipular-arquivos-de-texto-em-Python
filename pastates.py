inicio = 5
fim = 10
with open('numero.txt', 'r') as n:
    for numero in n: 
        num = n.readlines()
        
    
    inicio -= 1
    fim -= 1
        
for linha in num[inicio:fim]:
    print(linha.strip())