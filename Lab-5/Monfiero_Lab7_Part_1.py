number1=int(input('Enter first number here: '))
while number1<=0:
    number1=int(input('ERROR: Enter a positive integer here: '))

number2=int(input('Enter second number here: '))
while number2<=0:
    number2=int(input('ERROR: Enter a positive integer here: '))
sum=number1+number2
print('The sum of these two numbers is: ', sum)
product=number1*number2
print('The product of these two numbers is: ', product)
if number1>number2:
    print('The larger of the two numbers is: ', number1)
    big=number1
else:
    print('The larger of the two numbers is: ', number2)
    big=number2
if number1<number2:
    print('The smaller of the two numbers is: ',number1)
    small=number1
else:
    print('The smaller of the two numbers is: ',number2)
    small=number2
difference=small-big
print('The difference of the smaller number subtracted by the bigger number is: ', difference)
quotient=big/small
print('The quotient of the bigger number divided by the smaller is: %.2f' %quotient)
