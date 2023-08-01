row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

first_digit = int(position[0]) #column = 3
second_digit = int(position[1]) #row = 3

row = map[second_digit - 1]
row[first_digit-1] = 'X'


# if first_digit == 1 and second_digit == 1:
#     row1[0] = 'X'
# elif first_digit == 1 and second_digit == 2:
#     row2[0] = 'X'
# elif first_digit == 1 and second_digit == 3:
#     row3[0] = 'X'

# if first_digit == 2 and second_digit == 1:
#     row1[1] = 'X'
# elif first_digit == 2 and second_digit == 2:
#     row2[1] = 'X'
# elif first_digit == 2 and second_digit == 3:
#     row3[1] = 'X'

# if first_digit == 3 and second_digit == 1:
#     row1[2] = 'X'
# elif first_digit == 3 and second_digit == 2:
#     row2[2] = 'X'
# elif first_digit == 3 and second_digit == 3:
#     row3[2] = 'X'

print(f"{row1}\n{row2}\n{row3}")
