# average
count = None
sum = None
print("starting numbers:\n", count,"\nand\n", sum)
for value in [9,41,12,3,74,15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("final numbers:", count, sum)
print("average:", sum / count)