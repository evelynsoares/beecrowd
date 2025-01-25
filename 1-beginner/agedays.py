#1020
age = int(input())
years = age/365
months = (age%365)/30
days = (age%365)%30
print("%d ano(s)\n" %years + "%d mes(es)\n" %months + "%d dia(s)" %days)