adventure_type = input('What type of adventure should I have?')

if adventure_type == 'scary' or adventure_type == 'short':
    print("Entering the dark forest!")
elif adventure_type == 'safe' or adventure_type == 'long':
    print('Taking the safe route!')
else:
    print("Not sure which route to take.")