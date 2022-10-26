t = [9, 41, 12, 3, 74, 15] # list positions start with 0 in the first place
x = t[1:3] # slice and dice
y = t[:3] # up to but not including
z = t[3:] # starting at
w = t[:] # whole list
print(x,y,z,w)

# g = list()
# dir(g) # used to lookup things about list but doesn't seem to work right now probably doing something wrong