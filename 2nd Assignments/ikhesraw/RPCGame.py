import random

options = ['rock','paper','scissor']

def getInputs():
    p1 = input("Player 1, make your move:")
    
    if p1 not in options:
        print("Wrong input, please choose one of: [rock,paper,scissor]\n")
        return getInputs()

    p2 = options[random.randint(0,2)]

    if p2 not in options:
        print("Wrong input, please choose one of: [rock,paper,scissor]\n")
        return getInputs()
    print(f"Computer chose {p2}.\n")  

    return makeDecision(p1,p2)    

def makeDecision(p1,p2):
    if p1 == p2:
        return print("The game is Tigh!")
    elif p1 == options[0]:
        if p2 == options[1]:
            return print("Player 2 wins!")
        elif p2 == options[2]:
            return print('Player 1 wins!')
    elif p1 == options[1]:
        if p2 == options[0]:
            return print("Player 1 wins!")
        elif p2 == options[2]:
            return print('Player 2 wins!')
    elif p1 == options[2]:
        if p2 == options[0]:
            return print("Player 1 wins!")
        elif p2 == options[1]:
            return print('Player 2 wins!')                            
    else:
        return print("Something went wrong!")


getInputs()        