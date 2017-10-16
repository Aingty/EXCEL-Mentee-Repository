num_people=int(input('Enter how many people are attending the cookout.'))
num_hotdogs=int(input('Enter how many hotdogs per person.'))
total=num_people*num_hotdogs
num_bunpack=total//8
num_hotdogpack=total//10
if total % 8 != 0:
    num_bunpack += 1
if total % 10 !=0:
    num_hotdogpack += 1
remain_buns=(num_bunpack*8)-total
remain_hotdogs=(num_hotdogpack*10)-total
print('Minimum required packages of buns:',num_bunpack)
print('Minimum required packages of hotdogs:',num_hotdogpack)
print('Hotdog remainder:',remain_buns)
print('Bun remainder:',remain_hotdogs)




6
