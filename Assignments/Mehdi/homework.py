Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> var name = "Mehdi"
  File "<stdin>", line 1
    var name = "Mehdi"
        ^^^^
SyntaxError: invalid syntax
>>>  name = "Mehdi"
  File "<stdin>", line 1
    name = "Mehdi"
IndentationError: unexpected indent
>>>  a = "Mehdi"
  File "<stdin>", line 1
    a = "Mehdi"
IndentationError: unexpected indent
>>>  str = "Mehdi"
  File "<stdin>", line 1
    str = "Mehdi"
IndentationError: unexpected indent
>>>  name
  File "<stdin>", line 1
    name
IndentationError: unexpected indent
>>> name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'name' is not defined
>>> name = "mehdi"
>>> name
'mehdi'
>>> city = "kabul"
>>> city
'kabul'
>>> age = 21
>>> age
21
>>> percentage = 88
>>> percentage
88
>>>
>>> print(my name is {}, I was born in {}city, My age is{}, My school name was {}, I got {} number in previous semester)fomat(name,city,age,school,percentage)
  File "<stdin>", line 1
    print(my name is {}, I was born in {}city, My age is{}, My school name was {}, I got {} number in previous semester)fomat(name,city,age,school,percentage)
          ^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> school = "sidal nasiry"
>>> school
'sidal nasiry'
>>> print(my name is {}, I was born in {}city, My age is{}, My school name was {}, I got {} number in previous semester)fomat(name,city,age,school,percentage)
  File "<stdin>", line 1
    print(my name is {}, I was born in {}city, My age is{}, My school name was {}, I got {} number in previous semester)fomat(name,city,age,school,percentage)
          ^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("my name is {}, I was born in {}city, My age is{}, My school name was {}, I got {} number in previous semester")fomat(name,city,age,school,percentage")
  File "<stdin>", line 1
    print("my name is {}, I was born in {}city, My age is{}, My school name was {}, I got {} number in previous semester")fomat(name,city,age,school,percentage")
                                                                                                                                                               ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print("my name is {}, I was born in {}city, My age is{}, My school name was {}, I got {} number in previous semester")fomat(name,city,age,school,percentage")
  File "<stdin>", line 1
    print("my name is {}, I was born in {}city, My age is{}, My school name was {}, I got {} number in previous semester")fomat(name,city,age,school,percentage")
                                                                                                                                                               ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print("my name is {}, I was born in {}city, My age is{}, My school name was {}, I got {} number in previous semester")format(name,city,age,school,percentage")
  File "<stdin>", line 1
    print("my name is {}, I was born in {}city, My age is{}, My school name was {}, I got {} number in previous semester")format(name,city,age,school,percentage")
                                                                                                                                                                ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print("my name is {}, I was born in {}city, My age is{}, My school name was {}, I got {} number in previous semester").format(name,city,age,school,percentage")
  File "<stdin>", line 1
    print("my name is {}, I was born in {}city, My age is{}, My school name was {}, I got {} number in previous semester").format(name,city,age,school,percentage")
                                                                                                                                                                 ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print("my name is {}, I was born in {}city, My age is{}, My school name was {}, I got {} number in previous semester").format(name,city,age,school,percentage")
  File "<stdin>", line 1
    print("my name is {}, I was born in {}city, My age is{}, My school name was {}, I got {} number in previous semester").format(name,city,age,school,percentage")
                                                                                                                                                                 ^
SyntaxError: unterminated string literal (detected at line 1)
>>>
>>>
>>>
>>> name
'mehdi'
>>> city
'kabul'
>>> age
21
>>> school
'sidal nasiry'
>>> percent
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'percent' is not defined. Did you mean: 'percentage'?
>>> percentage
88
>>> print("my name is {}, I was born in {}city, My age is{}, My school name was {}, I got {} number in previous semester".format(name,city,age,school,percentage"))
  File "<stdin>", line 1
    print("my name is {}, I was born in {}city, My age is{}, My school name was {}, I got {} number in previous semester".format(name,city,age,school,percentage"))
                                                                                                                                                                ^
SyntaxError: unterminated string literal (detected at line 1)
>>> a ="my name is {}, I was born in {}city, My age is{}, My school name was {}, I got {} number in previous semester".format(name,city,age,school,percentage")
  File "<stdin>", line 1
    a ="my name is {}, I was born in {}city, My age is{}, My school name was {}, I got {} number in previous semester".format(name,city,age,school,percentage")
                                                                                                                                                             ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print("my name is {}, I was born in {}city, My age is{}, My school name was {}, I got {} number in previous semester".format(name,city,age,school,percentage))
my name is mehdi, I was born in kabulcity, My age is21, My school name was sidal nasiry, I got 88 number in previous semester
>>>
