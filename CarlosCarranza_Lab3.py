#Declare variables
books=0
points=0

#Receive user input and convert to integer//
books=int(input('Enter books:'))

#Check user's points awarded//
if (books < 2):
    points=0
elif (books >= 2 and books < 4):
    points=5
elif (books >= 4 and books < 6):
    points=15
elif (books >= 6 and books < 8):
    points=30
elif (books >= 8):
    points=60

#Display user's points awarded//
int(points)
print('You get',points,'points!')