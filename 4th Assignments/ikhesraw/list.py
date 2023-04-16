# 1- Program to sum all numbers in a list
list = [100,200,300,400,500]
total = 0
for num in list:
    total += num

print(total)

# 2- Program to get the largest number from a list
list2 = [4,7,2,9,10,80,11]
largest = list2[0]
for num in list2:
    if num > largest:
        largest = num

print(largest)        

# 3- program to print the numbers of a specified list after removing even numbers from it
list3 = [1,2,3,4,5,6,7,8,9,10]
list4 = []

for num in list3:
    if (num % 2) != 0:
        list4.append(num)

print(list4)        