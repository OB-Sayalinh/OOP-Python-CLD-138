days_in_month_list = [31, 28, 31, 30, 30, 30, 31, 29, 30, 31, 30, 31]

def is_year_leap(year): return not ((year % 4) or (not year % 100 and year % 400))

def days_in_month(year, month):
    # if month == 2 and is_year_leap(year): return days_in_month_list[month - 1] + 1
    # else: return days_in_month_list[month - 1]

    return days_in_month_list[month - 1] + (is_year_leap(year) and month == 2)

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
