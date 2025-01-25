#1013
a, b, c = input().split()
a, b, c = float(a), float(b), float(c)
maiorab = (a+b+(abs(a-b)))/2
maiorac = (a+c+(abs(a-c)))/2
maiorbc = (b+c+(abs(b-c)))/2
if maiorab > maiorac :
    print("%d eh o maior"  %maiorab)
elif maiorac > maiorbc :
    print("%d eh o maior" %maiorac)
else:
    print("%d eh o maior" %maiorbc)