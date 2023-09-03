def is_year_leap(year):
    divis_by_100 = False
    divis_by_400 = False
    century_test = False
    divis_by_4 = False
    

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        


def days_in_month(year, month):
    days_in_month = 0
    leap_year = False
    
    
    if is_year_leap(year):
        leap_year = True
    else:
        leap_year = False
    
    months_with_31 = [1, 3, 5, 7, 8, 10, 12]

    if month in months_with_31:
        days_in_month = 31
    elif month == 2:
        if leap_year == True:
            days_in_month = 29
        else:
            days_in_month = 28
    else:
        days_in_month = 30
    
    return days_in_month
    

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