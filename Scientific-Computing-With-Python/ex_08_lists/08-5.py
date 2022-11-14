# abc = 'With three words'
# stuff=abc.split() # splits into list at whitespace or spaces
abc ='with;three;words'
stuff=abc.split(';') # splits at defined thing, in this case a semi-colon(;) normal split looks for spaces
print(stuff)
print(stuff[0]) # prints position 0
print(len(stuff)) # tells us how many items are in the list (stuff)
for w in stuff: print(w) # prints each postion or item in list (stuff)