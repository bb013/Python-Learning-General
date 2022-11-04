# script calculates either the surface footage or the RPM depending on what is input.
print("This program is used to callculate speeds and feeds for use in manufacturing\nAre you trying to find the surface feet per minute, 'sfm', or are you trying to find the revolutions per minute, 'rpm'?")
var = str.lower(input("Please type either 'sfm' or 'rpm', without quotes, and then press enter: "))# str.lower accounts for case differences

while var not in ('sfm', 'rpm'):
    print('You typed something wrong')
    var = str.lower(input("Please type either 'sfm' or 'rpm', without quotes, and then press enter: "))# str.lower accounts for case differences
    """_summary_
    section accounts for if the input is different from that which is needed
    Returns:
        _type_: _description_
    """    
def diametertext():
    while var == 'rpm' or'sfm':
        try:
            dia = float(input('Diameter of what is spinning in inches '))
            return dia
        except:
            print("input error, numeric values only")
            continue
        break
    """_summary_
    section tries to convert to float and re-asks for input if it can't
    """    
# if 'rpm is desired
while var == 'rpm':
    dia = diametertext()
    while True:
        try:
            sfm = float(input('Desired Surface Feet Per Minute? '))
        except:
            print("input error, numeric values only")
            continue
        break
    rpm =  3.82 * sfm / dia # the math of calculating rpm
    print('rpm =', rpm, 'or rounded it is: ','rpm = ',round(rpm) )
    break
# if 'sfm' is desired
while var == 'sfm':
    dia = diametertext()
    while True:
        try:
            rpm = float(input('RPM of what is spinning? '))
        except:
            print("input error, numeric values only")
            continue
        break
    sfm = .262 * dia * rpm # the math of calculating surface feet per minute
    print('sfm =', sfm, 'or rounded it is: ','sfm = ',round(sfm))
    break