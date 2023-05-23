# First number is column, Second number is row. And this is what makes it a little bit difficult
# ................
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# ......................

#...........................
column=int(position[0])
row=int(position[1])

selected_row=map[row-1]
selected_row[column-1]="X"

#map[row-1][column-1]="X" #we can use this instead of the previous two lines

#..........................

# ..........................
print(f"{row1}\n{row2}\n{row3}")

