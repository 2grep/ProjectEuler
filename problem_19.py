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

year = 1901
months = [["January",31], ["March", 31], ["April", 30], ["May", 31], ["June", 30], ["July", 31], ["August", 31], ["September", 30], ["October", 31], ["November", 30], ["December", 31]]
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
day_of_week = "Monday"
julian_day = 1
days_in_month = months[0][1]
sequential_day = 1
day_date = [1900,1,1,"January",1,"Monday"]
for i in range (first_year, last_year):
    julian_day = 1
    month = "January"
    if i % 4 == 0:
        d = 366
        months.insert(1,["February", 29])
    else:
        d = 365
        months.insert(1,["February", 28])
    for j in range (0,len(months)):
        month = months[j]
        for k in range(0,len(month)):
            sequential_day += sequential_day
            julian_day += julian_day

for range  (days of month)
increment day_of_week
if day_of_week == "Sunday" and day_of_momth = 1:
    Sundays += 1

calendar = []
for i in range(1901,2001):
    calendar.append(i)
    if i % 4 == 0:
        d = 366
    else:
        d = 365
    days = [n+1 for n in range(0,d)]
    calendar.append(days)





