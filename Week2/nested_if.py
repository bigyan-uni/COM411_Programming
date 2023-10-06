book_type = input('What type of cover does the book have?')
bind_quality = input('Is the book perfect-bound?')
#  initiating variables and storing user input

if book_type == "soft":
    if bind_quality == "yes":
        print("Soft cover, perfect bound books are very popular!")
    elif bind_quality == 'no':
        print("Soft covers with coils or stitches are great for short books!")
elif book_type == 'hard':
    print('Books with hard covers can be more expensive!')
#  prints appropriate values based on the user inputs

