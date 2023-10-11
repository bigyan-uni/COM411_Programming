print('WHOLE NUMBER CALCULATIONS')
operation = input('What operation would you like to perform?')
firstnum = int(input('What is the first number?'))
secondnum = int(input('What is the second number?'))

if operation == '+':
    print(f'{firstnum} + {secondnum} = {firstnum + secondnum}')
elif operation == '-':
    if firstnum >= secondnum or firstnum - secondnum >= 0:
        print(f'{firstnum} - {secondnum} = {firstnum - secondnum}')
    else:
        print('Sorry. I have not learned integers yet.')
else:
    print("I don't know multiplication or division. Wait for the next update.")