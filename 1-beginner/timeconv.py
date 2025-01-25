#1019
time = int(input())
hours = time/3600
minutes = time%3600/60
seconds = (time%3600)%60
print("%d:" %(int(hours)) + "%d:" %(int(minutes)) + "%d" %(int(seconds)))