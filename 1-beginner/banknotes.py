#1018
N = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]
aux = N
print(N)

for i in notas :
    print("%d nota(s) de R$ " %int(aux/i) + "%d,00" %i)
    aux = aux%i