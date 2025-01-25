#1021
N = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

aux = N
print("NOTAS:")
for i in notas :
    print("%d nota(s) de R$ " %int(aux/i) + "%d.00" %i)
    aux = aux%i

aux += 0.001
print("MOEDAS:")
for i in moedas :
    print("%d moeda(s) de R$ " %int(aux/i) + "%.2f" %i)
    aux = aux%i