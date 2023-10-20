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