nums =10
for row in range(nums):
    for space in range(nums-row-1):
        print(" ",end="")
    for emoji in range(row+1):
        print("\U0001f600",end="")
    print()