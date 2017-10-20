#Declare variables
totalRainfall = 0.0
monthRainfall = 0.0
averageRainfall = 0.0
years = 0
totalMonths = 0

#Get number of years
years = int(input('Enter the number of years: '))

#Get rainfall per month
for year in range(years):
    print('For year ', year + 1, ':')
    for month in range(12):
        monthRainfall = float(input('Enter the rainfall amount for the month: '))
        #Accumulate months
        totalMonths += 1
        #Accumulate rainfall amount
        totalRainfall += monthRainfall

#Calculate average rainfall
averageRainfall = totalRainfall / totalMonths

print('For', totalMonths, 'months')
print('Total rainfall:', format(totalRainfall, '.2f'), 'inches')
print('Average monthly rainfall:', format(averageRainfall, '.2f'), 'inches')
