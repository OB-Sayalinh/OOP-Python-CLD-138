hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

all_hours = hour + ((mins + dura) // 60)
# Keeps hours under 24
clamped_hours = all_hours - ((all_hours // 24) * (24))

all_minutes = mins + dura
clamped_minutes = (mins + dura) - (((mins + dura) // 60) * (60))

print("Time is now:", str(clamped_hours) + ":" + str(clamped_minutes))

# Short Hand
#print("Time is now:", str((hour + ((mins + dura) // 60)) - (((hour + ((mins + dura) // 60)) // 24) * (24))) + ":" + str((mins + dura) - (((mins + dura) // 60) * (60))))