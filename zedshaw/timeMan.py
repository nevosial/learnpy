from datetime import datetime, time
now = datetime.now()
print("Current DateTime (YYYY-MM-DD HR:Min:Sec.milliseconds) :")
print(now)
print("Time (HR:Min:Sec.milliseconds):")
now_time = now.time()
print(now_time)


print("Check if the current time between 12:30 and 14:30 hrs....")
# Will check if the current time between 12:30 and 14:30 hrs.
if now_time >= time(12,30) and now_time <= time(14,30):
    print("Yes, current time is within interval specified !")
else:
    print("No, current time is not within interval specified.")
