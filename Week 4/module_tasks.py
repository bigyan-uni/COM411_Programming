#  defining function
def play_guess_the_number():
    #  importing module random
    import random

    #  initialising variables
    min_value = int(input('Please enter the minimum value: '))
    max_value = int(input("Please enter the maximum value: "))
    guess_correct = False
    random_value = random.randrange(min_value, max_value + 1, 1)

    #  loop to keep running until user guesses the correct number
    print(f"I am thinking of a number between {min_value} and {max_value}.  Can you guess what it is?")
    while guess_correct is False:
        user_value = int(input())
        if user_value < random_value:
            print("Your guess is too low.")
            print("Try again:")
        elif user_value > random_value:
            print("Your guess is too high.")
            print("Try again:")
        elif user_value == random_value:
            print('Congratulations! You guessed my number!')
            guess_correct = True
        else:
            print('Try again:')


#  calling function
play_guess_the_number()
