#testing some math funtions and type erors

#start of math
print('math order of operations are always \nParenthesis \nPower \nMultiplication or Division \nAdditon or Subtration \nand always done left to right')
print('For order of operations on 1 + 2 ** 3 / 4 * 5')
print("the '2 ** 3' is done first being a power. So two to the third power or 2 ** 3 = 8")
print('then division and multiplication is done left to right')
print('8 / 4 = 2')
print('2 * 5 = 10')
print('finaly addition is done left to right')
print('1 + 10 = 11')
print('below is the same equation only with python doing the work')
mathTest1 = 1 + 2 ** 3 / 4 * 5
type(mathTest1)
print(mathTest1)
print('since division is involved there is a floating point and the type becomes a float \nhowever below is the same thing forced to be an integer')
print(int(mathTest1)) #type forced to integer
#end of math

#start of types
eee = 'hello ' + 'there'
print(eee)
type(eee)
eRight = eee + '1' #this works because '1' is inside '' and therefore considered a string and python concatenates it with 'eee'
print(eRight)
type(eRight)
eWrong = eee + 1 #this doesn't work because python is trying to use mathmatic funtion 'add' because it sees that 1 is an integer
print(eWrong)