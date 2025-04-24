year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    if year // 4 != year / 4:
        print("Common Year")
    elif year % 100 != 0:
        print("Leap Year")
    elif round(year / 400) != year / 400:
        print("Common Year")
    else:
        print("Leap Year")