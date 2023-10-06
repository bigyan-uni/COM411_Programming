user_num = int(input('Please enter a whole number.'))

if user_num % 2 == 0:
    print(f'The number {user_num} is an even number.')
elif user_num % 2 == 1:
    print(f'The number {user_num} is an odd number')
else:
    print('Please input a valid whole number.')
#  Fallback message if user inputs invalid response
