days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_year_leap(year): return not ((year % 4) or (not year % 100 and year % 400))

def days_in_month(year, month): return days_in_month_list[month - 1] + (is_year_leap(year) and month == 2)

def day_of_year(year, month, day):
    if month <= 12 and day <= days_in_month(year, month):
        return sum(days_in_month_list[:month - 1]) + day + is_year_leap(year)
    else:
        return None
    # This would work by itself if I did not have to return none on invalid arguments
    # return sum(days_in_month_list[:month]) + day + is_year_leap(year)

print(day_of_year(2000, 12, 31))
print(day_of_year(2001, 12, 31))
print(day_of_year(1981, 29, 18))


