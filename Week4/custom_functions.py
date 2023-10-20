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


#  creating function to help the player cross the bridge
def cross_bridge(steps):
    for i in range(steps):
        print("Crossed step.")
    if steps > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")


#  calling function with example arguments
cross_bridge(3)
cross_bridge(6)


#  creating a function to help player climb the collapsed bridge, which is now conveniently a ladder
def climb_ladder(steps_remaining, steps_crossed):
    if steps_remaining > steps_crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")


#  calling function with more arguments
climb_ladder(5, 2)
climb_ladder(2, 5)


#  function to display ladder
def display_ladder(steps):
    print("| |\n***\n| |")
    print("***\n| |\n" * (steps - 1))


#  function to create ladder
def create_ladder():
    steps = input("How many steps remain?")
    display_ladder(int(steps))


#  calling create_ladder to test both functions
create_ladder()


# character in the adventure is trying to distribute their weight so they can reach the top of the bridge ladder quicker

def sum_weights(weight, inventory_weight):
    return int(weight) + int(inventory_weight)


def calc_avg_weight(weight, inventory_weight):
    return sum_weights(weight, inventory_weight) / 2


def run():
    user_weight = input('What is the weight of the person?')
    user_inventory_weight = input('What is the weight of their inventory?')
    decision = input("What would you like to calculate (sum or average)?")
    if decision == 'sum':
        print(sum_weights(user_weight, user_inventory_weight))
    elif decision == 'average':
        print(calc_avg_weight(user_weight, user_inventory_weight))


#  calling above function
run()


#  The character has now found a map, we wish to create functions that manipulate cryptic words#
def choose_option():
    print("1) Display in a Box")
    print("2) Display Lower-case")
    print("3) Display Upper-case")
    print("4) Display Mirrored")
    print("5) Repeat")
    option = input("Which type of decryption would you like use?")
    phrase = input("Enter cryptic word: ")
    if option == '1':
        box_display(phrase)
    if option == '2':
        lower_display(phrase)
    if option == '3':
        upper_display(phrase)
    if option == '4':
        mirror_display(phrase)
    if option == '5':
        repeat_display(phrase)


#  display the word in an ASCII art box
def box_display(phrase):
    print('~' * (len(phrase) + 2))
    print("~" + phrase + "~")
    print('~' * (len(phrase) + 2))


#  display the word in lower-case e.g. hello
def lower_display(phrase):
    print(phrase.lower())


#  display the word in upper-case e.g. HELLO
def upper_display(phrase):
    print(phrase.upper())


#  display the word with its mirrored word e.g. Hello | olleH
def mirror_display(phrase):
    r_phrase = ""
    for i in phrase:
        r_phrase = i + r_phrase
    phrase = phrase + " | " + r_phrase
    print(phrase)


# ask the user how many times to display the word and then display the word that many times alternating between
# upper-case and lower-case
def repeat_display(phrase):
    repeat_num = int(input('How many times do you want to display the word?'))
    is_upper = True
    for i in range(repeat_num):
        if is_upper is True:
            print(phrase.upper())
            is_upper = False
        else:
            print(phrase.lower())
            is_upper = True


#  calling choose option
choose_option()
