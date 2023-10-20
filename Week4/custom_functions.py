#  initialising listen function
def listen():
    sound = input('What sound did you hear?')
    print(f'That was a loud {sound}!')


#  calling listen function
listen()


#  initialising identify function
def identify():
    user_observation = input('What lies before us?')
    if user_observation == 'a large boulder':
        print("It's time to run!")
    else:
        print('We will be fine.')


#  calling identify function
identify()


#  initialising escape_by function
def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("We cannot escape that way! The boulder is in the way!")


#  calling function with solutions
escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")
