#  Logical OR Operator
adventure_type = input('What type of adventure should I have?')

if adventure_type == 'scary' or adventure_type == 'short':
    print("Entering the dark forest!")
elif adventure_type == 'safe' or adventure_type == 'long':
    print('Taking the safe route!')
else:
    print("Not sure which route to take.")

#  Logical AND Operator
user_listen = input("What did I hear?")
user_sight = input("What did I see?")

if user_listen == 'grr' and user_sight == 'two red eyes':
    print("There is a scary creature. I should get out of here!")
elif user_listen == 'hoot' and user_sight == 'some big eyes':
    print("It's just an owl.")
else:
    print("I am a little scared but I will continue.")
