def getNum():
    number1=input('Enter first number here: ')
    while number1.isdigit()==False:
        while number1<=0:
            number1=input('ERROR: Enter a positive integer here: ')
    number2=int(input('Enter second number here: '))
    while number2.isdigit()==False:
        while number2<=0:
            number2=int(input('ERROR: Enter a positive integer here: '))
def calcSum(number1, number2):
    sum=number1+number2
    return sum
def calcProduct(number1, number2):
    product=number1*number2
    return product
def displayMinNum(number1, number2):
    if number1<number2:
        small=number1
    else:
        small=number2
    return small
def displayMaxNum(number1, number2):
    if number1>number2:
        big=number1
    else:
        big=number2
    return big
def calcDifference(big, small):
    difference=small-big
    return difference
def calcQuotient(big, small):
    quotient=big/small
    return quotient
def displayResult(sum, product, small, big, difference, quotient):
    print('Sum is: ', sum)
    print('Product is: ', product)
    print('Smaller number is: ',small)
    print('Bigger number is: ', big)
    print('Difference is: ', difference)
    print('Quotient is: %.2f' %quotient)
def main():
    getNum()
    sum=calcSum(number1, number2)
    product=calcProduct(number1, number2)
    small=displayMinNum(number1, number2)
    big=displayMaxNum(number1, number2)
    difference=calcDifference(big, small)
    quotient=calcQuotient(big, small)
    displayResult(sum, product, small, big, difference, quotient)
main()