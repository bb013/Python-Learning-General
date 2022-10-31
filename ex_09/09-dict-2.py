#counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
#for key in counts:
#    if counts[key] > 10:
#        print(key, counts[key])

#counts = {}
#line =input('enter some text')
#words = line.split()
#print('Words: ', words)
#print('Counting')
#for eachline in words:
#    counts[eachline] = counts.get(eachline,0) + 1
#print('Counts', counts)

values = {'chuck' : 1, 'fred' : 42, 'jan': 100}
#for key in values:
#    print(key, values[key])
for aaa,bbb in values.items():
    print(aaa,bbb)