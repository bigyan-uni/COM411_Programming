#  First Program
book_genre = input("What type of book is this?")  # stores the genre of book

if book_genre == "adventure":
    print(f'I like {book_genre} books!')  # formatted string prints appropriate message


print("Finished reading book.")

#  Second Program
activity_type = input("Please enter the activity to be performed.")
#  stores user's input

if activity_type == "calculate":
    print("Performing calculations...")
    #  prints appropriate message
else:
    print("Performing activity...")
    #  prints alternative message
print('Activity completed!')

#  Third Program
user_direction = input('Towards which direction should I go (up, down, left or right)?')
#  stores direction user wishes to move towards

if user_direction == 'up':
    print('I am moving in an upward direction!')
elif user_direction == 'down':
    print('I am moving in a downward direction!')
elif user_direction == 'left':
    print('I am moving towards the left!')
elif user_direction == 'right':
    print('I am moving towards the right!')
else:
    print('That is not a valid direction.')
#  fallback message in case user inputs invalid direction


