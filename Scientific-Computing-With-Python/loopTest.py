import time #load definition for 'time'

def forLoop():
    #### start 'for' loop ####
    dramaticSentence = ["This", "is", "a", "dramatic", "sentence!"]
    for words in dramaticSentence:
            print(words)
            time.sleep(1) #one second delay
    print("Did you like it?")
    time.sleep(2)
    #### end 'for' loop ####

def whileLoop():
    #### start 'while' loop ####
    print('Starting Countdown')
    time.sleep(.5) #half second delay
    countDown = 5
    while countDown > 0:
        print(countDown)
        time.sleep(1) #one second delay added
        countDown = countDown - 1
    print('blast off!')
    time.sleep(2)
#### end 'while' loop ####

var = input("Choose loop type by typing either 'for' or 'while' and then press enter:  ") #asks to run either type of loop

while var not in ('for', 'while'): #creates a state to account for incorrect user input
    print("Incorrect input. Please try again.")
    var = input("Choose loop type by typing either 'for' or 'while' and then press enter:  ") #asks to run either type of loop
while var == 'for' or 'while':
    if var == 'for':
        forLoop()
        break # breaks out of loop
    if var == 'while':
        whileLoop()
        break # breaks out of loop
print('end of script')