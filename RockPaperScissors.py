import random

def impossible():    
    print ('Impossible')
    invalid = 0
    while invalid == 0:
        choice = input('Rock, Paper, Scissors: ')
        choice = choice.lower()
        if choice == 'rock':
            print ('Computer picks Paper \nComputer Wins!')
            invalid = 1
        elif choice == 'paper':
            print ('Computer picks Scissors \nComputer Wins!')
            invalid = 1
        elif choice == 'scissors':
            print ('Computer picks Rock \nComputer Wins!')
            invalid = 1
        else:
            print ('Choose Rock, Paper, or Scissors. \nTry again.')    

def randomChoice():
    print ('Random')
    win = 0
    while win == 0:
        choice = input ('Rock, Paper, Scissors: ')
        choice = choice.lower()
        options = ["rock","paper","scissors"]
        computerPick = random.choice(options)
        print ("Computer picks " + computerPick)
        if choice == computerPick: print ('Tie! Try again.')
        elif choice == 'rock':
            if computerPick == 'paper': print ('Computer Wins!')
            elif computerPick == 'scissors':
                print ('User Wins!')
                win = 1
        elif choice == 'paper':
            if computerPick == 'scissors': print ('Computer Wins!')
            elif computerPick == 'rock':
                print ('User Wins!')
                win = 1
        elif choice == 'scissors':
            if computerPick == 'rock': print ('Computer Wins!')
            elif computerPick == 'paper':
                print ('User Wins!')
                win = 1
        else: print ('Choose Rock, Paper, or Scissors. \nTry Again.')
def learning():
    print ('Learning')
    computerMemory = [[],[]]
    finish = 1 
    computerWin = 0
    found = 0
    options = ["rock","paper","scissors"]
    while finish == 1:
        while computerWin == 0:
            choice = input ('Rock, Paper, Scissors: ')
            choice = choice.lower()
            computerPick = ''
            if len(computerMemory[0]) > 0:
                for index,loggedUserHands in enumerate(computerMemory[0]):
                    if choice == loggedUserHands.lower():
                        computerPick = computerMemory[1][index]
                    
            if computerPick == '':
                computerPick = random.choice(options)
            print ("Computer picks " + computerPick)
            if choice == computerPick: print ('Tie! Try again.')
            elif choice == 'rock':
                if computerPick == 'paper':
                    print ('Computer Wins!')
                    computerWin = 1
                elif computerPick == 'scissors':
                    print ('User Wins!')
            elif choice == 'paper':
                if computerPick == 'scissors':
                    print ('Computer Wins!')
                    computerWin = 1
                elif computerPick == 'rock':
                    print ('User Wins!')
            elif choice == 'scissors':
                if computerPick == 'rock':
                    print ('Computer Wins!')
                    computerWin = 1
                elif computerPick == 'paper':
                    print ('User Wins!')
            else: print ('Choose Rock, Paper, or Scissors. \nTry Again.')
        for knownWins in computerMemory[0]:
            if knownWins == choice:
                found = 1
                computerWin = 0
                print('Computer already knows how to win this hand')
        if found == 0:
            computerMemory[0].append(choice)
            computerMemory[1].append(computerPick)
            print ('Computer now knows how to beat ' + choice)
        computerWin = 0
        found = 0
        finish = int(input('Would you like to keep playing:\n 1. Yes \n 2. No \n'))
        
mode = int(input('Choose the mode you would like to play:\n 1. Impossible \n 2. Random! \n 3. Adapt\n'))
if mode == 1:impossible()
elif mode == 2: randomChoice()
elif mode == 3: learning()
else: print('Please choose a valid option')
    
def learning():
    print ('Learning')
    mustBe = ['rock','paper','scissors']
    learnedWins = [[],[]]
    learn = 0
    while learn == 0:
        userIn = input('If user picks: ')
        check = 0
        while check == 0:
            for x in mustBe:
                if userIn.lower() == x:
                    check = 1
                    break
            if check == 0:
                print('Must be rock, paper, scissors.')
                check = 2
        if check == 1:
            computerOut = input('Then to win, computer picks: ')
            for known in learnedWins[0]:
                if userIn == known:
                    print ('Already learned how to beat: ' + known)
                    quit()
            learnedWins[0].append(userIn)
            learnedWins[1].append(computerOut)
            if len(learnedWins[0]) == 3:
                learn = 1
                print('All Done')
        else: quit()
    win = 0
    while win == 0:
        choice = input('Rock, Paper, Scissors: ')
        choice = choice.lower()
        computerPick = ''
        for index,search in enumerate(learnedWins[0]):
            if choice == search.lower():
                computerPick = learnedWins[1][index]
        print ("Computer picks " + computerPick)
        if choice == computerPick:
            print ('Tie! User Submitted Incorrect Win Condition.')
        elif choice == 'rock':
            if computerPick == 'paper':
                print ('Computer Wins!')
            elif computerPick == 'scissors':
                print ('User Wins! User Submitted Incorrect Win Condition.')
        elif choice == 'paper':
            if computerPick == 'scissors':
                print ('Computer Wins!')
            elif computerPick == 'rock':
                print ('User Wins! User Submitted Incorrect Win Condition.')
        elif choice == 'scissors':
            if computerPick == 'rock':
                print ('Computer Wins!')
            elif computerPick == 'paper':
                print ('User Wins! User Submitted Incorrect Win Condition.')
        else: print ('Choose Rock, Paper, or Scissors. \nTry Again.')
        retry = int(input('Try Again:\n1.Yes\n2.No'))
        if retry == 2:
            win == 1
        elif retry != 1:
            print('Incorrect choice: Now resetting.')
def adapt():
    print ('Adapt')
    win = 0
    pattern = []
    while win == 0:
        choice = input ('Rock, Paper, Scissors: ')
        choice = choice.lower()
        options = ["rock","paper","scissors"]
        computerPick = random.choice(options)
        print ("Computer picks " + computerPick)
        if choice == computerPick:
            print ('Tie! Try again.')
            pattern.append(computerPick)
        elif choice == 'rock':
            if computerPick == 'paper':
                print ('Computer Wins!')
                win = 1
                pattern.append(computerPick)
            elif computerPick == 'scissors':
                print ('User Wins!')
                pattern.append(computerPick)
        elif choice == 'paper':
            if computerPick == 'scissors':
                print ('Computer Wins!')
                win = 1
                pattern.append(computerPick)
            elif computerPick == 'rock':
                print ('User Wins!')
                pattern.append(computerPick)
        elif choice == 'scissors':
            if computerPick == 'rock':
                print ('Computer Wins!')
                win = 1
                pattern.append(computerPick)
            elif computerPick == 'paper':
                print ('User Wins!')
                pattern.append(computerPick)
        else: print ('Choose Rock, Paper, or Scissors. \nTry Again.')
        print(pattern)
    while win == 1:
        if len(pattern) > 0:   
            computerPick = pattern.pop(0)
        else: computerPick = random.choice(options)
        choice = input ('Rock, Paper, Scissors: ')
        choice = choice.lower()
        print ("Computer picks " + computerPick)
        if choice == computerPick: print ('Tie! Try again.')
        elif choice == 'rock':
            if computerPick == 'paper':
                print ('Computer Wins!')
                win = 2
            elif computerPick == 'scissors':
                print ('User Wins!')
        elif choice == 'paper':
            if computerPick == 'scissors':
                print ('Computer Wins!')
                win = 2
            elif computerPick == 'rock':
                print ('User Wins!')
        elif choice == 'scissors':
            if computerPick == 'rock':
                print ('Computer Wins!')
                win = 2
            elif computerPick == 'paper':
                print ('User Wins!')
        else: print ('Choose Rock, Paper, or Scissors. \nTry Again.')