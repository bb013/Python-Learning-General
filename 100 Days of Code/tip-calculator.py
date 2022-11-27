print('A tip calculator')
# ask for total and makes sure it is a float with 2 decimal places
total = round(float(input('What is the total bill? $')), 2)

# asks how many ways it will be split
split = int(input('How many ways is the bill being split? '))

# optional # prints your portion of the tip with 2 decimal places
your_bill_split = round(total/split, 2 )
print(f'Your part of the bill is ${your_bill_split} ')

# converts what is entered to percentage and finds tip amount rounded to 2 decimal places
tip_choice = float(input('What percentage of a tip would you like to leave? '))/100
tip_total = round(tip_choice * your_bill_split, 2)

# calculates, formats, and prints out the totals
your_total_bill = (1+tip_choice) * your_bill_split
# formatting to two decimal places
your_total_bill = "{:.2f}".format(your_total_bill)
print(f'Your tip is ${tip_total} making your total bill be ${your_total_bill} ')