temps = [[0.0 for h in range(24)] for d in range(31)]
# 24 rows of hourly temps for 31 columns of days

#PRETEND MATRIX DATA IS MAGICALLY FILLED W VALUES

#determine monthly average noon temperatures
total = 0.0
#assume midnight temps are stored first

#passes through temps matrix and assign day list w/ subsequent rows of matrix
for day in temps:
    #index of 11 is to access the temp value at noon (12) which is index 11
    total += day[11]
    
    
#set the initial highest temp to -100 to hold our updated highest temp as we iterate
highest = -100

#iterate through days in temp
for day in temps:
    #iterate through temps (hours) in day columns
    for temp in day:
        #see if the temp for each hour is higher than our current highest recorded
        if temp > highest:
            #if the hours temp is higher than highest, replace highest w it
            highest = temp
#print the highest temp after we have iterated over all days and their hours
print("The highest temperature was: " , highest)



#temporary variable to store how many days were > 20 deg celcius
hot_days = 0

#iterate over all days in our matrix
for day in temps:
    #check if the noon temp of that day was > 20 deg celcius
    if day[11] > 20.0:
        #if it was increment the number of hot days by one
        hot_days += 1
        
#print how many days were "hot"  AKA over 20 deg celcius at noon

print(hot_days, "days were hot.")