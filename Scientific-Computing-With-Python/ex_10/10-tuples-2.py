# / ANCHOR - finds 10 most used words and prints

# opens file with simple error check while loop
while True:
    try:
        fhand = open(input('Enter file name: '))
        break
    except:
        print("Didn't catch that.")
        continue
# empty dictionary named counts
counts = dict()

# looks at file line by line
for eachline in fhand:
    # splits each line into words
    words = eachline.split()
    # adds each word to dictionary 'counts' If already there adds 1 to the value
    for eachword in words:
        counts[eachword] = counts.get(eachword, 0)+1


# This line can replace all the commented out code below
lst = sorted( [ (v,k) for k,v in counts.items() ], reverse=True )

"""
## begin replaced code

# empty list named lst
lst = list()

# looks at the items in counts dictionary
for key, val in counts.items():
    # creates tuples with reversed value compared to counts dictionary
    newtup = (val, key)
    # appends each of the tuples to list 'lst'
    lst.append(newtup)
# sorts list in decending order
lst = sorted(lst, reverse=True)

## end replaced code
"""
# prints first 10 items out of the now sorted list 'lst'
for val, key in lst[:10]:
    # notice the switched positions
    print(key, val)