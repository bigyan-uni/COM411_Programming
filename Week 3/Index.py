#  initiating variables
user_word = input('What word do you see?')

print('Displaying index positions...')

#  for loop
for position in range(0, len(user_word), 1):

    print(f'index {position}: {user_word[position]}')

#  final message
print('Done!')

