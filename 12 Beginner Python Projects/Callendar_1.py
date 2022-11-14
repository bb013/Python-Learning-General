# Select which day of the week the calendar starts on and then displays the callendar
# Current selection is limited to Sunday or Monday
# Didn't finish all days of the week because that wasn't the point of this experiment
# Leaving parially done instead of deleting whole file in case I wan't to come back and add other weedays
import calendar
def day_set(var):
    settheday = var
    if settheday not in range(7):
        print("some serious mistakes were made")
        quit()        
    if settheday == 0:
        calendar.setfirstweekday(0) # set first day of week
    if settheday == 1:
        calendar.setfirstweekday(1) # set first day of week
    if settheday == 2:
        calendar.setfirstweekday(2) # set first day of week
    if settheday == 3:
        calendar.setfirstweekday(3) # set first day of week
    if settheday == 4:
        calendar.setfirstweekday(4) # set first day of week
    if settheday == 5:
        calendar.setfirstweekday(5) # set first day of week
    if settheday == 6:
        calendar.setfirstweekday(6) # set first day of week
    yy = 2022 # year
    mm = 11 # month
    # display the calendar
    print(calendar.month(yy, mm))
#### modify this section for other days of the week
x = input('Select M or S: ')
x = str.lower(x)
print(f'you selected {x}')
if x==('m'):var=0
if x==('s'):var=6
if x not in ('s', 'm'):
    print("some f'n thing went wrong")
    #quit()
### end section to modify
day_set(var)