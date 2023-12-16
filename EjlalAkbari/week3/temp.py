import random

userChoicesList = list()
computerChoicesList = list()
gameTuple = ["Rock", "Scissors", "Paper"]
gameRound = 0
roundOfGame = 0
print('=' * 40)
print('please note that you have to know \nsome rules before playing RPS game!')
print('-' * 40)
print('Rock smashes Scissors \nScissors cut Paper \nPaper covers Rock')
print('-' * 40)
print('=' * 40)
inp = input('Do you want to play? (y/n):')
while True:
    if inp.lower() == 'y':
        print('thanks')
        while True:
            inp = input('How many rounds do you want to play?')
            if inp.lower() == 'q' or inp.lower() == 'quit':
                break
            if not inp.isdigit():
                print('Please enter an integer number')
            if inp.isdigit():
                gameRound = int(inp)
                print(f'gameRound: {gameRound}')
                while roundOfGame < gameRound:
                    temp = gameRound
                    print(f'Round: {roundOfGame}')
                    inp = input('Please enter yur choice: \nR or Rock --> Rock\nP or Paper --> Paper\nS or Scissors '
                                '--> Scissors\n')
                    if inp.lower() == 'r' or inp.lower() == 'rock':
                        userChoicesList.append('Rock')
                        computerChoicesList.append(random.choice(gameTuple))
                        print(f'In round {roundOfGame} you have chosen {userChoicesList[roundOfGame]}')
                        print(f'In round {roundOfGame} computer has chosen {computerChoicesList[roundOfGame]}')
                        roundOfGame += 1
                    if inp.lower() == 'p' or inp.lower() == 'paper':
                        userChoicesList.append('Paper')
                        computerChoicesList.append(random.choice(gameTuple))
                        print(f'In round {roundOfGame} you have chosen {userChoicesList[roundOfGame]}')
                        print(f'In round {roundOfGame} computer has chosen {computerChoicesList[roundOfGame]}')
                        roundOfGame += 1
                    if inp.lower() == 's' or inp.lower() == 'scissors':
                        userChoicesList.append('Scissors')
                        computerChoicesList.append(random.choice(gameTuple))
                        print(f'In round {roundOfGame} you have chosen {userChoicesList[roundOfGame]}')
                        print(f'In round {roundOfGame} computer has chosen {computerChoicesList[roundOfGame]}')
                        roundOfGame += 1
                    if not inp.lower() == 'r' and not inp.lower() == 'rock' and not inp.lower() == 'p' \
                            or not inp.lower() == 'paper' and not inp.lower() == 's' or \
                            not inp.lower() == 'scissors':
                        print('you have entered wrong entry!')
                    while True:


    elif inp.lower() == 'n':
        print('goodbye')
        break
    else:
        print('Sorry but you have entered wrong entry')
        inp = input('Please enter correct entry y/n:')
