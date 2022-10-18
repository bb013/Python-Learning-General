sh = input("Enter Hours: ")
try:
    fh = float(sh)
except:
    quit("input error, numeric numbers only")
sr = input("Enter Rate: ")
try:
    fr = float(sr)
except:
    quit("input error, numeric numbers only")
# print(fh, fr)
if fh > 40 :
    # print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 1.5) # exercise has it written as (fr * 0.5) but that is incorrect and would only account for the overtime portion of the extra hours.
    #print(reg,otp)
    xp = reg + otp
else:
    # print("Regular")
    xp = fr * fh
print("Pay:",xp)