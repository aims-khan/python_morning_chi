row_nuns = 10

for row in range(row_nums):
for space in range (row_nuns-row-1):
	print("",end="")
for emoji in range(row+1):
	print("\U0001f600",end="")
print()		