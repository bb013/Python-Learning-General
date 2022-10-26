# fhand = open('ex_07_1\L00099100-3.NCF') # used to open a constant file name
count = 0
fname = input('Enter a file name to open: ') # used to prompt for file name to open
    # following try-except block could be used a 'quit' command instead of 'continue' if it used outside of a while loop
try:
    fhand = open(fname) # opens given file name
except:
    print('File "',fname,'" cannot be opended.')
    quit()
for cheese in fhand:
    count = count+1 ## used if you want to count the number of lines
print('Line count', count) ## print the number of lines