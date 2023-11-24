#  initiating variables, getting input
bars_to_charge = int(input("How many bars should be charged?"))
bars_charged = 0

#  while loop
while bars_to_charge != bars_charged:
    print("Charging: ", end='')
    bars_charged += 1
    print('█ ' * bars_charged)

#  final message
print('The battery is fully charged.')