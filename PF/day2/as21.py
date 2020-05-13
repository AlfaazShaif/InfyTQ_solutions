# PF-Tryout
# assignment21-level-3

def generate_next_date(day,month,year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        leap_year = True
    else:
        leap_year = False
    
    if month in (1,3,5,7,8,10,12):
        days_in_month = 31
    elif month == 2:
        if leap_year:
            days_in_month = 29
        else:
            days_in_month = 28
    else:
        days_in_month = 30

    if day < days_in_month:
        day = day + 1
    else:
        if month == 12:
            day = 1
            month = 1
            year = year + 1
        else:
            day = 1
            month = month + 1

    next_day = day
    next_month = month
    next_year = year

    print(next_day,"-",next_month,"-",next_year)


generate_next_date(31,12,2019)