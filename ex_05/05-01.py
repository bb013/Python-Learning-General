# average
#count = None
#sum = None
#print("starting numbers:\n", count,"\nand\n", sum)
#for value in [9,41,12,3,74,15]:
#    count = count + 1
#    sum = sum + value
#    print(count, sum, value)
#print("final numbers:", count, sum)
#print("average:", sum / count)

# Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number or "done", the mistake is detected using try and except and prints an error message then skips to the next number
added=0
count=0
while True:
    number=input("Enter a number: ")
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