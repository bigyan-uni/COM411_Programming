print("Program Started!")
character = input("Please enter an ASCII code: ")
character = abs(int(character))

if character in range(32, 127):
    code = chr(character)
    print(f"The character represented by the ASCII code {code} is {character}.")
else:
    print('The input you have given is not within range. Try again next time.')

print('Program ended.')
