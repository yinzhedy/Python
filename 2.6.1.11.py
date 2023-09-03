hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
start_time_minutes = (hour * 60) + mins
end_time_total_mins = start_time_minutes + dura
end_time_hour = end_time_total_mins // 60
end_time_minutes = end_time_total_mins % 60
end_time = str(str(end_time_hour) + ":" + str(end_time_minutes))
print(str(end_time))