row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column_pick = (int(position[0])-1)
row_pick = int(position[1])

if(row_pick == 1):
    row1[column_pick] = "🔳"
elif(row_pick == 2):
    row2[column_pick] = "🔳"
else:
    row3[column_pick] = "🔳"

print(f"{row1}\n{row2}\n{row3}")