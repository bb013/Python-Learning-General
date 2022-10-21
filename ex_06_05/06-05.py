string = 'X-DSPAM-Confidence: 0.8475 '
fspace = string.find(': ')
#print(fspace)# debug check 1
number=string[fspace+1 :]
#print(number)# degub check 2
fnumber=float(number)
print(fnumber)