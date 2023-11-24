user_observation = input("Where should I look?")
if user_observation == 'in the bedroom':
    if input('Where in the bedroom should I look?') == 'under the bed':
        print("Found some shoes but no phone.")
    else:
        print('Found some mess but no phone.')
elif user_observation == 'in the bathroom':
    if input("Where in the bathroom should I look?") == 'in the bathtub':
        print("Found a rubber duck but no phone")
    else:
        print("Found bathroom stuff but no phone.")
elif user_observation == "in the living room":
    if input("Where in the living room should I look?") == 'on the table':
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but no phone.")
else:
    print("I do not know where that is but I will keep looking.")

