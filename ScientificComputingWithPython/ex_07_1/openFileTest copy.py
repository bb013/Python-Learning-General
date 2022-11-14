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
wholefile = fhand.read() # .read comand reads the whole file
print(wholefile)
print(len(wholefile)) # len tells you the letter count