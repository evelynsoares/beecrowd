#1038
code, amount = map(float, input().split())

print("Total: R$ ", end="")
if code == 1:
    print("%.2f" %(amount*4))
elif code == 2:
    print("%.2f" %(amount*4.5))
elif code == 3:
    print("%.2f" %(amount*5))
elif code == 4:
    print("%.2f" %(amount*2))
else:
    print("%.2f" %(amount*1.5))
