# script calculates either the surface footage or the RPM depending on what is input.
print("Are you trying to find the surface feet per minute, 'sfm', or are you trying to find the revolutions per minute, 'rpm'?")
var = input("Please type either 'sfm' or 'rpm', and then press enter. Case sensitive: ")
# section to account for incorrect input
while var not in ('sfm', 'rpm'):
    print('You typed something wrong')
    var = input("Please type either 'sfm' or 'rpm', and then press enter. Case sensitive: ")
# end incorrect input section
# if 'rpm is desired
while var == 'rpm':
    dia = input('Diameter of what is spinning in inches: ')
    sfm = input('Desired Surface Feet Per Minute? ')
    rpm =  3.82 * float(sfm) / float(dia)
    print('rpm =', rpm, 'or truncated it is: ','rpm = ',int(rpm) )
    break
# if 'sfm' is desired
while var == 'sfm':
    dia = input('Diameter of what is spinning in inches ')
    rpm = input('RPM of what is spinning? ')
    sfm = .262 * float(dia) * float(rpm)
    print('sfm =', sfm, 'or truncated it is: ','sfm = ',int(sfm))
    break
