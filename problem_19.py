# You are given the following information, but you may prefer to do some research for yourself.
# 
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# 
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# Calculate the number of days in each year.
# List the Julian days
# Label each day with the month - catch leap years
# label each day with the day-of-week

# Significant strategy change: rather than enumerating every data and iterating 
# through them to find the interesting datas, just count those dates as they
# are generated, and store on the minimal necessary counters.

def feb_correct(year):
    months = [["January",31], ["March", 31], ["April", 30], ["May", 31], ["June", 30], ["July", 31], ["August", 31], ["September", 30], ["October", 31], ["November", 30], ["December", 31]]
    if year % 4 == 0:
        months.insert(1,["February", 29])
    else:
        months.insert(1,["February", 28])
    return months

def sunday_firsts(year, days_from_beginning):
    first_sundays = []
    months = feb_correct(year)
    day_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    julian_day = 0 # not necessary but keeping it for debugging
    month = []
        for j in range (0,len(months)):
        month = months[j]
        for k in range(1,months[j][1]+1):
            days_from_beginning += 1
            julian_day += 1
            day_date = [days_from_beginning,year,julian_day,month[0],k,day_of_week[int(days_from_beginning) % 7]]
            if day_date[5] == "Sunday" and day_date[4] == 1:
                first_sundays.append(day_date)
            result = [first_sundays, days_from_beginning]
    return result

def main():
    first_sundays = []
    days_from_beginning = 0
    for year in range(1901,2001):
        result = sunday_firsts(year, days_from_beginning)
        first_sundays.append(result[0])
        days_from_beginning = int(result[1])
    first_sundays = [item for sublist in first_sundays for item in sublist]
    return first_sundays

main()