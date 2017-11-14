def calcSum(number1, number2):
    sum=number1+number2
    print('Sum is: ',sum)
def calcProduct(number1, number2):
    product=number1*number2
    print('Product is: ',product)
def displayMinNum(number1, number2):
    if number1<number2:
        small=number1
        print(small,' is the smaller number')
    else:
        small=number2
        print(small,' is the smaller number')
def displayMaxNum(number1, number2):
    if number1>number2:
        big=number1
        print(big,' is the bigger number')
    else:
        big=number2
        print(big,' is the bigger number')
def calcDifference(number1, number2):
    if number1>number2:
        big=number1
    else:
        big=number2
    if number1<number2:
        small=number1
    else:
        small=number2
    difference=small-big
    print('Difference is: ', difference)
def calcQuotient(number1, number2):
    if number1>number2:
        big=number1
    else:
        big=number2
    if number1<number2:
        small=number1
    else:
        small=number2
    quotient=big/small
    print('Quotient is: %.2f' %quotient)
def main():
    number1=int(input('Enter first number here: '))
    while number1<=0:
        number1=int(input('ERROR: Enter a positive integer here: '))
    number2=int(input('Enter second number here: '))
    while number2<=0:
        number2=int(input('ERROR: Enter a positive integer here: '))
    calcSum(number1, number2)
    calcProduct(number1, number2)
    displayMinNum(number1, number2)
    displayMaxNum(number1, number2)
    calcDifference(number1, number2)
    calcQuotient(number1, number2)
main()