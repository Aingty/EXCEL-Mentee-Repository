print (" You need at least 8 characters long \n Must contain one uppercase letter \n Must contain one lower case letter \n Must contain one numeric digit \n No Spaces")

x = True
while (x == True):
    p = input("Please type a password a strong password \n\t") 
    digit = 0
    lower = 0
    upper = 0
    space = 0
    for i in p:
        if i.isdigit():
            digit = 1 
        if i.islower():
            lower = 1
        if i.isupper():
            upper = 1
        if i.isspace():
            space = 1
    if digit==1 and lower==1 and space==0 and upper==1 and len(p) >= 8:
        print("Password Valid :)")
        x = False
    else:
        print("Password Incorrect")
        



            
            
            
            

     
           

     