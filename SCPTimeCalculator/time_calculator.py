def add_time(startHour, duration, startDay=""):
    # Key: sh = startHour, dur = duration, sd = startDay, hr = hour
    week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    # Initialize variables
    newTime = ""
    weekDay = ""
    plusDays = ""
    plusHours = ""
    daysAdded = ""

    # Extract start hour, minute, and format
    shHour, shMinute, shFormat = startHour.split(":")[0], startHour.split(":")[1][:2], startHour[-2:]

    # Extract duration hour and minute
    durHour, durMinute = duration.split(":")[0], duration.split(":")[1]

    # Convert extracted values to integers for calculations
    shHourInt, shMinuteInt, durHourInt, durMinuteInt = map(int, [shHour, shMinute, durHour, durMinute])

    # Calculate result minute
    resultMinute = (shMinuteInt + durMinuteInt) % 60

    # Adjust start hour for PM format
    if shFormat == "PM":
        shHourInt += 12

    # Calculate total hours
    plusHours = shHourInt + durHourInt + ((shMinuteInt + durMinuteInt) // 60)

    # Ensure result minute is formatted as a string with leading zero if needed
    resultMinute = str(resultMinute).zfill(2)

    # Calculate days to add
    plusDays = plusHours // 24

    # Determine the result day string
    if plusDays > 0:
        daysAdded = "(next day)" if plusDays == 1 else "({n} days later)".format(n=plusDays)

    # Calculate result hour
    resultHour = plusHours % 24

    # Determine the format (AM/PM) and adjust hour accordingly
    if resultHour >= 12:
        shFormat = "PM"
        if resultHour > 12:
            resultHour -= 12
    else:
        shFormat = "AM"
        if resultHour == 0:
            resultHour = 12

    # Determine the day of the week if provided
    if startDay.lower() in week:
        weekDay = week[(week.index(startDay.lower()) + plusDays) % 7]

    # Construct the newTime string
    newTime = "{hour}:{minute} {format}".format(hour=resultHour, minute=resultMinute, format=shFormat)

    # Include the day of the week and additional day information if applicable
    if weekDay:
        newTime = newTime + ", " + weekDay.title()
    if plusDays > 0:
        newTime = newTime + " " + daysAdded

    return newTime.rstrip()
