#  initiating variables, getting input
obstacles_to_avoid = int(input('How many obstacles must I avoid?'))
obstacles_avoided = 0

#  while loop
while obstacles_to_avoid != obstacles_avoided:
    print('Avoiding...', end='')
    print(f'...Done! {obstacles_avoided + 1} obstacles avoided.')
    obstacles_avoided += 1
print('All obstacles have been avoided.')
