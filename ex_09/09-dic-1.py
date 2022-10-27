##### Video question code
#counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
#print(counts.get('kris', 0))
#### End video question code
dicname = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for datainput in names:
    if datainput not in dicname:
        dicname[datainput] = 1
    else:
        dicname[datainput]=dicname[datainput]+1
print(dicname)