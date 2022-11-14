"""
(x,y)=(4,'Fred') # tuples can be on the left side. When creating like this it is important to have the same number of items on both sides of the '='
print(y)
"""
d=dict()
d['johnny boy']=2
d['marrie-anne']=4
for key1,value1 in d.items():
    print(key1,value1)
tups=d.items() #d.items is a tuple
print(tups)