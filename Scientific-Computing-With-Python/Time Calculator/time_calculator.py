# Status = probably 80% complete with two TODO's left

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

    original_time_hours_minutes = original_time_split[0].split(":")
    original_hours = int(original_time_hours_minutes[0])
    original_minutes = int(original_time_hours_minutes[1])

    
    # find hours, minutes of duration time
    time_to_add_hours_minutes = time_to_add.split(":")
    time_to_add_hours = int(time_to_add_hours_minutes[0])
    time_to_add_minutes = int(time_to_add_hours_minutes[1])

    # add minutes and if needed add to hours
    totaled_minutes = original_minutes + time_to_add_minutes
    while totaled_minutes > 59:
        totaled_minutes -= 60
        time_to_add_hours += 1

    # Covert to 24 hour format
    if am_pm_var == 'PM':
        original_hours += 12
    
    # adds hours together
    totaled_hours = original_hours + time_to_add_hours
    
    # how many days of time added
    days_added = 0
    while totaled_hours > 23:
        totaled_hours -= 24
        days_added += 1

    # what day of week it now is
    if weekday != None:
        weekday_index_before_cleanup = original_weekday_indexed + days_added
        while weekday_index_before_cleanup > 6:
            weekday_index_before_cleanup -= 7
        final_weekday = weekday_index_before_cleanup

    # converts to 12 hour format
    if totaled_hours > 12:
        totaled_hours -= 12
        am_pm_var = 'PM'
    else:
        am_pm_var = 'AM'
    
    # TODO: verify that these outputs match what is needed
    # next day or not
    if days_added > 0:
        if days_added == 1:
            days_later_var = "next day"
        else:
            days_later_var = str(days_added)+" days later"
    else: days_later_var = "same day"

    # TODO: create variable "new_time" with everything in it. Take into account if there is or is not a weekday input

    return new_time

print(add_time("11:06 PM", "2:02", "Monday"))