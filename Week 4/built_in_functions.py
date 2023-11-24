print("Program Started!")
letter = input("Please enter a standard character:")

if len(letter) != 1:
    print('The input you have given is not one character. Try again next time.')
else:
    value = ord(letter)
    print(f'The ASCII code for {letter} is {value}.')
print('Program ended.')