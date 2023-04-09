for num in range(1, 21):
    if num == 4 or num == 13:
        print(f"{num} is unlucky")

    if (num % 2) == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
