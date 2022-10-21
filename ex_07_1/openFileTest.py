fhand = open('ex_07_1\L00099100-3.NCF')
count = 0
for cheese in fhand:
    #print(cheese)
    count = count+1
    #replaceorfind = cheese.find(input('what would you like to find? ')) # not working yet
    #print(replaceorfind) # not working yet
print('Line count', count)