#Obtain the number of hours worked within the week
hours_worked = float(input("Enter number of hours worked this week: "))
#Obtain hourly wage
hourly_rate = float(input("Enter hourly pay: "))
#For employee's who work over 40 hours
overtime = float(hours_worked*hourly_rate*1.5)

if hours_worked < 40:
    print("Employwee's weekly gross:", (hours_worked*hourly_rate))
else:
    print("Employee's gross including overtime hours:", overtime)
    
