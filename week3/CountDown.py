#  initiating variables
steps_remain = int(input("How far are we from the target?"))

#  for loop
for i in range(steps_remain, 0, -1):
    print(f'{i} steps remaining')

#  final message
print('Target achieved!')

