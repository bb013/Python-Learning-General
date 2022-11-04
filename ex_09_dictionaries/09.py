fname=input('Enter File: ')
if len(fname)<1:fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)
    for w in wds:
        """
        To start with, a variable (w) in the for statement refers to the item at the 0 index in the sequence(wds)
        The block of statements with increased uniform indent after the : symbol will be executed.
        A variable (w) now refers to the next item and repeats the body of the loop till the sequence is exhausted.
        or another way of saying it
        for each iterable(wds) create a variable called(w)
        An iterator is essentially a value producer that yields successive values from its associated iterable object.
        The built-in function next() is used to obtain the next value from in iterator.
        """
        # idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1
        #print(w,'new',di[w])

        """
        #verbose way of doing the same thing as above
        
        oldcount = di.get(w,0) # if the key isn't there we assume/make the count 0
        print(w,'old',oldcount)
        newcount = oldcount + 1
        di[w] = newcount
        print(w,'new',newcount)
        """
        """
        #even more verbose way of doing it:

        if w in di: # if the varable value (w) is in dictionary add + 1
            print('**',w,di.get(w,-99))
            di[w] = di[w] + 1
            print('***existing***')
        else: # if the varable value (w) is NOT in dictionary insert it and give it a value of 1
            di[w] = 1
            print('***new***')
        print(w,di[w])
        """
# print(di) ## verify that the data look good

# now we want to find the most common word

largest = -1
theword = None
for k,v in di.items():
    # print(k,v)
    if v > largest:
        largest = v
        theword = k
print(theword,largest)