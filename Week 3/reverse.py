#  initiating variables
user_str = input('What phrase do you want to see in reverse?')
reverse_str = ''

#  for loop
print('Reversing...')
for i in range(len(user_str) - 1, -1, -1):
    reverse_str += user_str[i]

#  final message
print('The phrase is: ' + reverse_str)