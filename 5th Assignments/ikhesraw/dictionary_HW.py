# First HW
info = {
    'name':'abc',
    'city':'kabul',
    'country':'afghanistan',
}
print({(k.upper() if k == 'country' else k):v for k,v in info.items()})

# Second HW
dict2 = dict(first=25, second=50, third=25, fourth=40, sixth=60)
sum = 0
for v in dict2.values():
    sum +=v
print(sum)

# Third HW
list1 = ['KBL', 'GZN', 'PRWN']
list2 = ['Kabul', 'Ghazni', 'Parwan']
list3 = {list1[i]:list2[i] for i in range(len(list1))}
print(list3)

# Fourth HW
vowels = ['A','E','I','O','U']
vowels_list = {vowels[i]: 0 for i in range(len(vowels))}
print(vowels_list)