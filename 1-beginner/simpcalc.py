#1010
code, unit, price = input().split()
code2, unit2, price2 = input().split()
print("VALOR A PAGAR: R$ %.2f" %((float(unit)*float(price)+float(unit2)*float(price2))))