# script calculates either the surface footage or the RPM depending on what is input.
print("This program is used to callculate speeds and feeds for use in manufacturing\nAre you trying to find the surface feet per minute, 'sfm', or are you trying to find the revolutions per minute, 'rpm'?")
var = input("Please type either 'sfm' or 'rpm', without quotes, and then press enter. Case sensitive: ")
# section to account for input other than 'sfm' or 'rpm'
while var not in ('sfm', 'rpm'):
    print('You typed something wrong')
    var = input("Please type either 'sfm' or 'rpm', without quotes, and then press enter. Case sensitive: ")
# end incorrect input section for sfm and rpm
# if 'rpm is desired
while var == 'rpm':
    while True: # this loop will account for input that isn't a number
        try:
            dia = float(input('Diameter of what is spinning in inches: '))
        except:
            print("input error, numeric values only")
            continue
        break
    while True:
        try:
            sfm = float(input('Desired Surface Feet Per Minute? '))
        except:
            print("input error, numeric values only")
            continue
        break
    rpm =  3.82 * sfm / dia
    print('rpm =', rpm, 'or truncated it is: ','rpm = ',int(rpm) )
    break
# if 'sfm' is desired
while var == 'sfm':
    while True: # this loop will account for input that isn't a number
        try:
            dia = float(input('Diameter of what is spinning in inches '))
        except:
            print("input error, numeric values only")
            continue
        break
    while True:
        try:
            rpm = float(input('RPM of what is spinning? '))
        except:
            print("input error, numeric values only")
            continue
        break
    sfm = .262 * dia * rpm
    print('sfm =', sfm, 'or truncated it is: ','sfm = ',int(sfm))
    break
