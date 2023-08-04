row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]
map_array = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

splitted_position = list(map(int, position))

if splitted_position[0] == 1 and splitted_position[1] == 1:
    row1[splitted_position[0] - 1] = 'X'
elif splitted_position[0] == 1 and splitted_position[1] == 2:
    row2[splitted_position[0] - 1] = 'X'
elif splitted_position[0] == 1 and splitted_position[1] == 3:
    row3[splitted_position[0] - 1] = 'X'
elif splitted_position[0] == 2 and splitted_position[1] == 1:
    row1[splitted_position[0] - 1] = 'X'
elif splitted_position[0] == 2 and splitted_position[1] == 2:
    row2[splitted_position[0] - 1] = 'X'
elif splitted_position[0] == 2 and splitted_position[1] == 3:
    row3[splitted_position[0] - 1] = 'X'
elif splitted_position[0] == 3 and splitted_position[1] == 1:
    row1[splitted_position[0] - 1] = 'X'
elif splitted_position[0] == 3 and splitted_position[1] == 2:
    row2[splitted_position[0] - 1] = 'X'
elif splitted_position[0] == 3 and splitted_position[1] == 3:
    row3[splitted_position[0] - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")

