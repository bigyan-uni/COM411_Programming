first_num = int(input('Please enter the first whole number.'))
second_num = int(input('Please enter the second whole number.'))
third_num = int(input('Please enter the third whole number.'))
even_counter = 0
#  initiate variables and store user inputs

if first_num % 2 == 0:
    even_counter += 1
if second_num % 2 == 0:
    even_counter += 1
if third_num % 2 == 0:
    even_counter += 1
#  increment counter upon encountering even number

print(f'There were {even_counter} even and {3 - even_counter} odd numbers.')