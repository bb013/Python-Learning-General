# fhand = open('ex_07_1\L00099100-3.NCF') # used to open a constant file name
while True: # loop to account for entering bad file names
    fname = input('Enter a file name to open: ') # used to prompt for file name to open
    # following try-except block could be used a 'quit' command instead of 'continue' if it used outside of a while loop
    try:
        fhand = open(fname) # opens given file name
        break # breaks out of while loop
    except:
        print('File "',fname,'" cannot be opended.')
        continue #used to restart while loop if except conditions met
count = 0
findit = input("Ask and you shall receive! What shall I find? ")
findit = findit.upper() # converts to uppercase
for cheese in fhand:
    #print(cheese.rstrip().upper()) # strips whitespace and makes everthing uppercase (won't work with current version of program, just leaving for reference)
    #count = count+1 ## used if you want to count the number of lines
    cheese = cheese.rstrip() # strips whitespace right side of line
    if not findit in cheese:# if line doesn't match 'findit' it restarts the loop otherwise will print any line that does contain 'findit'
        continue
    print(cheese)
    #if cheese.startswith(findit): # starts with
     #   print(cheese) # starts with
#print('Line count', count) ## print the number of lines
#wholefile = fhand.read() # .read comand reads the whole file
#print(wholefile)
#print(len(wholefile)) # len tells you the letter count