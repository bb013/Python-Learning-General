while True: # loop to account for entering bad file names
    fname = input('Enter a file name to open: ') # used to prompt for file name to open
    try:
        fhand = open(fname) # opens given file name
        break # breaks out of while loop
    except:
        print('File "',fname,'" cannot be opended.')
        continue #used to restart while loop if except conditions met
findit = input("Ask and you shall receive! What shall I find? ")
findit = findit.upper() # converts to uppercase
for cheese in fhand:
    cheese = cheese.rstrip() # strips whitespace right side of line
    if not findit in cheese: continue # if line doesn't match 'findit' it restarts the loop otherwise will print any line that does contain 'findit'
    print(cheese)