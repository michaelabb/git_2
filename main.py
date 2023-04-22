langs = ['Java','Python','JavaScript']
amount = [14,3,6]

dict = {}
combination = zip(langs,amount)
for (k,v) in combination:
    dict[k]=v
print(dict)

print({k:v for (k,v) in zip(langs,amount)})