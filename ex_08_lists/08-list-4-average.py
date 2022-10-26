## uses some list funtions to find an average
number = list()
while True:
    inp = input('Enter a number or enter done: ')
    inp=inp.lower()
    if inp=='done': break
    value=float(inp)
    number.append(value)
average = sum(number)/len(number)
print('Average',average)

## below is file 05-01 which does a similar thing but uses less memory and can account for more mistakes
quit() # quits program before running below code
# Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number or "done", the mistake is detected using try and except and prints an error message then skips to the next number
added=0
count=0
while True:
    number=input("Enter a number: ")
    number=number.lower()# this accounts for case differences
    if number == "done":
        if count==0:
            quit("no datat entered")# this accounts for when "done" is the first thing entered.
        break
    try:
        fnum=float(number)
    except:
        print("input error")
        continue
    count=count+1
    added=added+fnum
print(added, count, added/count)