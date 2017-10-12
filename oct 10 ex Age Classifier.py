#Obtain age from user: Age Classifier
age = int(input("Please enter the age of desired person: "))

if age <= 1:
    print ("Individual is a an infant")
if age > 1 and age < 13:
    print ("Person is a a child")
if age >= 13 and age < 20:
    print ("This human being is a teenager")
if age >= 20:
    print ("This user is classified as an adult")
