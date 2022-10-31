name = input('Enter file: ') # prompts for file to open
handle = open(name) # opens file
counts = dict() # creates blank dictionary
for eachline in handle: # start of loop through each line of open file
    words = eachline.split() # reads through opened file line at a time because it is split at each space by th 'split()' command
    for eachword in words: # reads each line split into each word
        counts[eachword] = counts.get(eachword,0) + 1 # adds each word to dictionary with a value this is a histagram
bigcount = None # prime next loop
bigword = None
for eachword,count in counts.items(): # looks through your 'counts' dictionary and looks at the key:(eachword) and the value:(count)
    if bigcount is None or count>bigcount:
        bigword = eachword # max loop
        bigcount = count
print(bigword,bigcount)