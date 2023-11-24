#  initiating variables
req_brightness = int(input('What level of brightness is required?'))
n = 0
print('Adjusting brightness...')

#  for loop
for i in range(2, req_brightness + 1, 2):
    print('Brightness level : ', end='')
    n += 1
    print('**' * n )
#  even settings only


#  printing final message
print('Complete!')