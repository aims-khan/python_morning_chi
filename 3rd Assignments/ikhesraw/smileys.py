# for i in range(10):
#     emoji = "\U0001f600"*i
#     print(emoji)
row_nums = 10
for row in range(row_nums):
    for space in range(row_nums-row-1):
        print(" ",end="")
    for emoji in range(row+1):
        print("\U0001f600",end="")
    print()        