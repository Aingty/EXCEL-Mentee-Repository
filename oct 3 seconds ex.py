seconds = 0
days = 0
hours = 0
minute = 0
dayRemainder = 0
minuteReamainder = 0
hourRemainder = 0
#Asks the user to input seconds
seconds = float(input("User, Enter the amount of seconds you wish to test: "))

if seconds >= 86400:
    days = seconds // 86400
    dayRemainder = seconds % 86400

if seconds >= 3600:
    hours = seconds // 3600
    hourRemainder = seconds % 3600

if seconds >=60:
    minutes = seconds // 60
    minuteRemainder = seconds % 60

if minute == 0:
    print(seconds, "Seconds equal to: ")
else:
    print(minutes, "full minutes and", minuteRemainder, "seconds")
    if hours != 0:
        print (hours, "full hours and", hourRemainder, "seconds")
    if days != 0:
        print (days, "full days and", dayRemainder, "seconds")
