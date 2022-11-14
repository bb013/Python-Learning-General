def computepay(hours, rate):
    if fh > 40 :
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 1.5) # exercise has it written as (fr * 0.5) but that is incorrect and would only account for the overtime portion of the extra hours.
        print(reg,otp)
        pay = reg + otp
    else:
        rate = rate * hours
    print("retruning",pay)
    return pay
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
# print(fh, fr)
xp = computepay(fh,fr)
print("Pay:",xp)
