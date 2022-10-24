fhand = open('ex_07_1\L00099100-3.NCF')
count = 0
findit = input("Ask and you shall receive! What shall I find? ")
for cheese in fhand:
    #count = count+1 ## used if you want to count the number of lines
    if cheese.startswith(findit):
                print(cheese)
#print('Line count', count) ## print the number of lines
#wholefile = fhand.read() # .read comand reads the whole file
#print(wholefile)
#print(len(wholefile))