##### Video question code
#counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
#print(counts.get('kris', 0))
#### End video question code

### first example tried in video
#dictinfo = dict()
#names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
#for data in names:
#    if data not in dictinfo:
#        dictinfo[data] = 1
#    else:
#        dictinfo[data]=dictinfo[data]+1
#print(dictinfo)
### end first example

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
#key, val = your_input.split(':')
#counts.update({key:value})
for name in names:
    counts[name] = counts.get(name, 0) + 1
#    if name in counts:
#        x = counts[name]
#    else:
#        x = 0
#x = counts.get(name, 0)
print(counts)
#quit()