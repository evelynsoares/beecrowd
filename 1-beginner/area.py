#1012
a, b, c = input().split()
pi = 3.14159
a, b, c = float(a), float(b), float(c)
print("TRIANGULO: %.3f\n" %(a*c/2) + "CIRCULO: %.3f\n" %(pi*c**2) + "TRAPEZIO: %.3f\n" %((a+b)*c/2) + "QUADRADO: %.3f\n" %(b*b) + "RETANGULO: %.3f" %(a*b))