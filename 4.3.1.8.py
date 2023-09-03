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


error_list = []

def check_input_validity(year, month, day):
    
    valid_num_length_test = False

    if len(str(year)) == 4:
        if len(str(month)) in range(1,3):
            if len(str(day)) in range(1,3):
                valid_num_length_test = True
            else:
                error_list.append("Day value failed length test, you entered: " + str(day))
        else:
            error_list.append("Month value failed length test, you entered: " + str(month))
    else:
        error_list.append("Year value failed length test, you entered:" + str(year))
        
    valid_num_range_test = False
    
    if year >= 1582:
        if month in range(1,13):
            if day in range(1,32):
                valid_num_range_test = True
            else:
                error_list.append("Day value failed range test, you entered: " + str(day))
        else:
            error_list.append("Month value failed range test, you entered:" + str(month))
    else:
        error_list.append("Year value failed range test, you entered:" + str(year))
    
    passed_tests = False
    
    if valid_num_length_test and valid_num_range_test:
        passed_tests = True
    else:
        return passed_tests
    
    return passed_tests
    
def day_of_year(year, month, day):
    
    passed_validity_test_function = check_input_validity(year, month, day)
    
    
    if passed_validity_test_function:
        print("Input of: month ", month, ", day ", day, ", and year ", year ,". Passed validity test")
    else:
        print("Input is not valid, please enter a valid year, month, and day (in that order)")
        print("Your input failed in the following ways: \n ", str(error_list))
        return None
        
    total_days = 0
    
    if passed_validity_test_function:
        for i in range(1, month + 1):
            total_days += days_in_month(year, i)
    else:
        return None
    
    return total_days
    
    
print(day_of_year(2000, 12, 31))
print(day_of_year(900, 77, 42))
