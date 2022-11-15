def seconds_since_midnight(hours=0, minutes=0, seconds=0):
    ## Hourss
    if 'am'.casefold() in str(hours) or 'pm'.casefold() in str(hours):
        if 'am'.casefold() in str(hours):
            hours = int(hours[:2])
        elif 'pm'.casefold() in str(hours):
            if '12'not in str(hours):
                hours += int(hours[:2]) + 12
            else:
                hours = 12
    hours_in_seconds = hours*3600
    ## Minutes
    minutes_in_seconds = minutes*60

    return hours_in_seconds + minutes_in_seconds + seconds

