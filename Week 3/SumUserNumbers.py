#  initiating variables
user_num = int(input("How many numbers should I sum up?"))
running_total = 0
counter = 1

#  creating while loops
while user_num >= counter:
    running_total += int(input(f'Please enter number {counter} of {user_num}:'))
    counter += 1

#  printing final message
print('The answer is ' + str(running_total))
