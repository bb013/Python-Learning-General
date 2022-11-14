#### code as pressented in exercise:
#sh = input("Enter Hours: ")
#sr = input("Enter Rate: ")
#fh = float(sh)
#fr = float(sr)
## print(fh, fr)
#if fh > 40 :
#    # print("Overtime")
#    reg = fr * fh
#    otp = (fh - 40.0) * (fr * 1.5) # exercise has it written as (fr * 0.5) but that is incorrect and would only account for the overtime portion of the extra hours.
#    print(reg,otp)
#    xp = reg + otp
#else:
#    # print("Regular")
#    xp = fr * fh
#print("Pay:",xp)
#### end exercise code

# below is a the same code cleaned up a little
fh = float(input("Enter Hours: "))
fr = float(input("Enter Rate: "))
if fh > 40 :
    # print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 1.5)
    xp = reg + otp
else:
    # print("Regular")
    xp = fr * fh
print("Pay:",xp)