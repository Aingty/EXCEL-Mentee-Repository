def getNum():
    number1=input("Enter a number you want to use for the selected function: ")
    while number1.isdigit()==False:
        number1=input("ERROR: Enter a positive integer here: ")
    number1=int(number1)
    return number1
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
def menu():
    keepGoing = True
    print("1 - Add")
    print("2 - Multiply")
    print("3 - Min")
    print("4 - Max")
    print("5 - Subtract")
    print("6 - Divide")
    print("7 - Quit")
    
    while keepGoing:
        operations=input("Choose a number between 1 through 7: ")
        if operations=="1":
            number1=getNum()
            number2=getNum()
            sum=calcSum(number1, number2)
            print("Sum is: ", sum)
        elif operations=="2":
            number1=getNum()
            number2=getNum()
            product=calcProduct(number1, number2)
            print("Product is: ", product)
        elif operations=="3":
            number1=getNum()
            number2=getNum()
            small=displayMinNum(number1, number2)
            print("The smaller number is: ", small)
        elif operations=="4":
            number1=getNum()
            number2=getNum()
            big=displayMaxNum(number1, number2)
            print("The bigger number is: ", big)
        elif operations=="5":
            number1=getNum()
            number2=getNum()
            big=displayMaxNum(number1, number2)
            small=displayMinNum(number1, number2)
            difference=calcDifference(big, small)
        elif operations=="6":
            number1=getNum()
            number2=getNum()
            big=displayMaxNum(number1, number2)
            small=displayMinNum(number1, number2)
            quotient=calcQuotient(big, small)
            print("Quotient is: %.2f" %quotient)
        elif operations=="7":
            keepGoing=False
        else:
            print('Error: Invalid value!')
menu()
            
            
        

        
