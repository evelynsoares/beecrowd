#1043
a, b, c = input().split(" ")
a, b, c = float(a), float(b), float(c)

if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("Area = %.1f" %((a+b)*c/2))
else:
    print("Perimetro = %.1f" %(a+b+c))
