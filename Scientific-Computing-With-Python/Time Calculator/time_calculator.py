def add_time(start, duration, weekday = None):
    # rename variables for clarity
    original_time = start
    time_to_add = duration
    
    # weekday given an indexed position
    weekday_list = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if weekday != None:
        original_weekday = weekday.capitalize()
        original_weekday_indexed = weekday_list.index(original_weekday)
    
    # find hours, minutes, and am or pm of starting time
    original_time_split = original_time.split()
    am_pm_var = original_time_split[-1].upper()
    if am_pm_var == "AM":
        am = True
    else: am = False

    # split things up and name
    original_time_hours_minutes = original_time_split[0].split(":")
    original_hours = int(original_time_hours_minutes[0])
    original_minutes = int(original_time_hours_minutes[1])

    # find hours, minutes of duration time
    time_to_add_hours_minutes = time_to_add.split(":")
    time_to_add_hours = int(time_to_add_hours_minutes[0])
    time_to_add_minutes = int(time_to_add_hours_minutes[1])

    # 24 hour formatting
    if am == False:
        original_hours += 12
    if (am == True) and (original_hours == 12):
        original_hours -= 12

    # adds hours together
    totaled_hours = original_hours + time_to_add_hours

    # add minutes and if needed add to hours
    totaled_minutes = original_minutes + time_to_add_minutes
    while totaled_minutes > 59:
        totaled_minutes -= 60
        totaled_hours += 1

    # how many days of time added
    days_added = 0
    while totaled_hours >= 24:
        totaled_hours -= 24
        days_added += 1

    # final am pm state
    if totaled_hours >= 12:
        final_am_pm_state = "PM"
    else: final_am_pm_state = "AM"

    # tweak the final displayed hours
    if totaled_hours > 12:
        totaled_hours -= 12
    if totaled_hours == 0:
        totaled_hours = 12

    # what day of week it now is
    if weekday != None:
        weekday_index = original_weekday_indexed + days_added
        while weekday_index > 6:
            weekday_index -= 7
        final_weekday = weekday_list[weekday_index]

    # next day or not
    if days_added > 0:
        if days_added == 1:
            days_later_var = "(next day)"
        else:
            days_later_var = "("+str(days_added)+" days later)"

    # usable number formatting for minutes
    formatted_minutes = "{0:0>2}".format(totaled_minutes)
    
    if (days_added == 0):
        if weekday != None:
            new_time = f"{totaled_hours}:{formatted_minutes} {final_am_pm_state}, {final_weekday}"
        else:
            new_time = f"{totaled_hours}:{formatted_minutes} {final_am_pm_state}"
    else:
        if weekday != None:
            new_time = f"{totaled_hours}:{formatted_minutes} {final_am_pm_state}, {final_weekday} {days_later_var}"
        else:
            new_time = f"{totaled_hours}:{formatted_minutes} {final_am_pm_state} {days_later_var}"

    return new_time

print(add_time("8:16 PM", "466:02", "tuesday"))