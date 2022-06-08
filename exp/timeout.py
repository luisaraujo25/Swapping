def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)

def getMonth(month):

    if month == "January":
        return 1
    elif month == "February":
        return 2
    elif month == "March":
        return 3
    elif month == "April":
        return 4
    elif month == "May":
        return 5
    elif month == "June":
        return 6
    elif month == "July":
        return 7
    elif month == "August":
        return 8
    elif month == "September":
        return 9
    elif month == "October":
        return 10
    elif month == "November":
        return 11
    elif month == "December":
        return 12
    else:
        return 0
    

def getTimeDict(time):

    #June 3, 2022, 6:43 p.m.
    indexMonth = findnth(time,' ', 0)
    month = time[0:indexMonth]
    indexDay = findnth(time, ',', 0)
    day = int(time[indexMonth+1:indexDay])
    indexYear = findnth(time, ',', 1)
    year = int(time[indexDay+2:indexYear])
    indexHour = findnth(time, ' ', 3)
    indexMinute = findnth(time, ':', 0)
    hour = int(time[indexYear+2:indexMinute])
    minute = int(time[indexMinute+1:indexHour])
    m = time[indexHour+1:len(time)-1]

    month = getMonth(month)
    if m == "p.m" and hour != 12:
        hour += 12
    elif m == "p.m" and hour == 12:
        hour = 00
    

    time = {
        'year': year,
        'month': month, 
        'day': day,
        'hour': hour,
        'minute': minute,
        'm': m
    }
    
    return time


print(getTimeDict("June 3, 2022, 6:43 p.m."))