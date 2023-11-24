#  initiating rows and columns
rows = int(input('How many rows should I have?'))
columns = int(input('How many columns should I have?'))

#  for loop
print('Here I go: ')
for i in range(0,rows):
    for j in range(0, columns):
        print(':-) ', end='')
    print('')

#  final message
print('Done!')
