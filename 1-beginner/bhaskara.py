#1036
import math 
a, b, c = map(float, input().split())

if ((b**2)-(4*a*c)) < 0 or a == 0:
    print("Impossivel calcular")
elif ((b**2)-(4*a*c) == 0):
    r = (-b + math.sqrt((b**2)-(4*a*c)))/(2*a)
    print("R1 = %.5f" %r)
    print("R2 = %.5f" %r)
else :
    r1 = (-b + math.sqrt((b**2)-(4*a*c)))/(2*a)
    r2 = (-b - math.sqrt((b**2)-(4*a*c)))/(2*a)
    print("R1 = %.5f" %r1)
    print("R2 = %.5f" %r2)
