#  Description : Program should calculate the numbers of characters in a sequence between two markers.

#  Getting markers and sequence
marker = input("Please enter the character for the marker: ")
user_sequence = input("Please enter a sequence of characters surrounded by above markers: ")

#  initiating other important variables
markers_seen = 0
is_marker = False
distance = 0

#  Nesting WHILE loop inside FOR loop
for char in user_sequence:
    if char == marker:
        markers_seen += 1
        is_marker = True
    else:
        is_marker = False
    while markers_seen == 1 and is_marker == False:
        distance += 1
        is_marker = True

#  Output
print(f"Distance between markers in sequence is {distance}.")