#First Program
book_genre = input("What type of book is this?")  # stores the genre of book

if book_genre == "adventure":
    print(f'I like {book_genre} books!')  # formatted string prints appropriate message


print("Finished reading book.")

#Second Program
activity_type = input("Please enter the activity to be performed.")
#stores user's input

if activity_type == "calculate":
    print("Performing calculations...")
    #prints appropriate message
else:
    print("Performing activity...")
    #prints alternative message
print('Activity completed!')
