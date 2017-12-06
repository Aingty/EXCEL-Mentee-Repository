#8.11
mystring='abcdefghijklmnopqrstuvwxyz'
if 'd' in mystring:
    print('Success')
else:
    print('Failure')
#8.12
big='ABCDEFGHI'
little=big.lower()
print(little)
#8.13
ch=input('Enter number or letter here: ')
digitreal=False
for i in ch:
    if i.isdigit():
        digitreal=True
if digitreal:
    print('Digit.')
else:
    print('No digit.')
