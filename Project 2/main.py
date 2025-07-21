
def add_time(start, duration, day_of_week=None):
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    
    time, period = start.split()
    start_hour, start_minute = map(int, time.split(":"))

   
    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    
    duration_hour, duration_minute = map(int, duration.split(":"))

    
    end_minute = start_minute + duration_minute
    extra_hour = end_minute // 60
    end_minute %= 60

    end_hour = start_hour + duration_hour + extra_hour
    days_later = end_hour // 24
    end_hour %= 24

    
    period = "AM"
    if end_hour >= 12:
        period = "PM"
    if end_hour > 12:
        end_hour -= 12
    elif end_hour == 0:
        end_hour = 12

    
    new_day = ""
    if day_of_week:
        day_index = days.index(day_of_week.capitalize())
        new_day_index = (day_index + days_later) % 7
        new_day = ", " + days[new_day_index]

    
    if days_later == 1:
        later = " (next day)"
    elif days_later > 1:
        later = f" ({days_later} days later)"
    else:
        later = ""

    
    new_time = f"{end_hour}:{str(end_minute).zfill(2)} {period}{new_day}{later}"
    return new_time
