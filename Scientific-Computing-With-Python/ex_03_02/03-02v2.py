# similar to 03-02 except the with some loops to allow for trying again on the input.
while True:
    try:
        fh = float(input("Enter Hours: "))
    except:
        print("input error, numeric values only")
        continue
    break
while True:
    try:
        fr = float(input("Enter Rate: "))
    except:
        print("input error, numeric values only")
        continue
    break
if fh > 40 :
    # print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 1.5)
    #print(reg,otp)
    xp = reg + otp
else:
    # print("Regular")
    xp = fr * fh
print("Pay:",xp)