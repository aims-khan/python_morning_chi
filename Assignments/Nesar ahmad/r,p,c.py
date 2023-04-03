import random
options = ['rock', 'paper' 'cessor']
print("Choose One of the curent moves\nrock\npaper\ncessor")
p1 = input("Player one make your move: ")

#p2 = input("Player two make your move: ")
rand_num = random.randint(0,2)
if rand_num == 0:
    p2 = 'rock'
elif rand_num == 1:
    p2 = 'paper'
elif rand_num == 2:
    p2 ='cessor'
print('\n Computer selected ->',p2)
if p1 not in options:
    print("player one wrong move!")

if p1 not in options:
    print("player two wrong move !")

if p1 == p2 :
    print("tigh!!")
elif p1 == 'rock' and p2 == 'paper':
    print("player 2 wins")
elif p1 == 'rock' and p2 == 'cessor':
    print("player one wins")
elif p1 == 'paper' and  p2 =='rock':
    print("player one wins")
elif p1 =='paper' and p2=='cessor':
    print("player twon wins")
elif p1 =='cessor' and p2 =='rock':
    print("player two wins")
elif p1 =='cessor'and p2 =='paper':
    print("player one wins")

else:
    print("wrong input")

