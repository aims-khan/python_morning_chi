for i in range(1, 21):
    user_input = input("Please enter a number: ")
    number = int(user_input)
    if number == 4 or number == 13:
        print(" X is unlucky.")
    elif number % 2 == 0:
        print(" X is even.")
    else:
        print(" X is odd.")
