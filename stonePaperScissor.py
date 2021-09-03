import random

def computerTurn():
    turn = ''
    randomNo = random.randint(1,3)
    if randomNo == 1:
        turn = 's'
    elif randomNo == 2:
        turn = 'p'
    elif randomNo == 3:
        turn = 'c'
    return turn    

def fullForm(x):
    if x == 's':
        return 'stone'
    elif x == 'p':
        return 'paper'
    elif x == 'c':
        return 'scissor'
    else:
        return 'wrong letter'

def whoWins(comp,player):
    win = None
    # if players choose same entities
    if comp == player:
        win = None
    # possible results
    elif comp == 's':
        if player == 'p':
            win = True
        elif player == 'c':
            win = False
    elif comp == 'p':
        if player == 's':
            win = False
        elif player == 'c':
            win = True
    elif comp == 'c':
        if player == 's':
            win = True
        elif player == 'p':
            win = False
    return win 

compPoints =  0
playerPoints = 0
match = 'Y'
while match=='Y':
    print('..................Welcome to Stone Paper and Scissor Game.....................')
    print('Computer\'s Turn : stone(s) paper(p) or scissor(c) ?')
    a = computerTurn()
    print('Computer has Selected ')
    b = input('Player\'s Turn : stone(s) paper(p) or scissor(c) ? ')
    print('Computer choose : '+fullForm(a))
    print('You choose : '+fullForm(b))
    c = whoWins(a,b)
    if c==None :
        print('Tie')
    elif c :
        print('You Won!')
        playerPoints +=1
    else:
        print('You Lose...')
        compPoints +=1
    match = input('Enter Y to Play again : ').upper()
    print()

print('\n..................SCORE.....................')
print('YOU\t\tCOMPUTER')
print(f'{playerPoints}\t\t{compPoints}')