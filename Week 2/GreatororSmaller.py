first_num = int(input('Please enter the first number.'))
second_num = int(input('Please enter the second number.'))

if first_num > second_num:
    print('The second number is the smallest!')
elif second_num > first_num:
    print('The first number is the smallest!')
elif first_num == second_num:
    print('Both are equal!')
else:
    print('Something went wrong. Try again later.')