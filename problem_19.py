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

calendar = []
for i in range(1901,2001):
    calendar.append(i)
    if i % 4 == 0:
        d = 366
    else:
        d = 365
    days = [n+1 for n in range(0,d)]
    calendar.append(days)





