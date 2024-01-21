import random

# =================================================================
validChoices = {'rock': 'Rock',
                'r': 'Rock',
                'paper': 'Paper',
                'p': 'Paper',
                'scissors': 'Scissors',
                's': 'Scissors',
                'quit': 'quit',
                'q': 'quit'}
# =================================================================
compChoicesTuple = 'rock', 'paper', 'scissors'
# =================================================================
userWinMessage = "What a lot of luck, wish you would not do that!"
userWinCount = 0
compWinMessage = "clap,clap,happiness, I'm the best!"
compWinCount = 0
tieMessage = "It's a tie! Seems our choices were the same."
# =================================================================
welcomeMessage = """Welcome to my game,
Here you have a chance to play the game of Rock-Paper-Scissors
Rules are simple:
    - Rock smashes Scissors
    - Scissors cut Paper
    - Paper covers Rock
Hope you enjoy it!"""
# =================================================================
winningScore = 0
scoredRounds = 0
totalGameRounds = 0
# =================================================================
print('\n' + '*' * 62)
print(welcomeMessage)
print('*' * 62)
# =================================================================
while True:
    inp = input('\nDo you want to start the game? (Y/N): ')
    if inp.lower() == 'n':
        print('\n' + '+' * 62)
        print('Hope you play this game another time :)')
        print('+' * 62)
        break
    if inp.lower() == 'y':
        proceed = True
        # user selected YES the game process starts:
        while proceed:
            winningScore = input('\nPlease type in a value for the winning score: ')
            if not winningScore.isdigit():
                print('I need an integer to carry on. Please type in an \"integer\" value')
                continue

            else:
                winningScore = abs(int(winningScore))
                if not winningScore:
                    print('I need a "NON ZERO" integer to carry on. Please type in a \"non-zero integer\" value')
                    continue

                # user entered winningScore, start to get choices:
                while True:
                    rockCount = 0
                    paperCount = 0
                    scissorsCount = 0
                    quitCount = 0

                    userEntry = input('\nPlease select either Rock(R), Paper(P), Scissors(S) or Quit(Q) to exit: ')
                    userChoiceLowerWordsList = [word.lower() for word in userEntry.split()]

                    # want to count the occurrence of each validChoices values:
                    for w in userChoiceLowerWordsList:
                        if w in validChoices:
                            if validChoices[w] == 'Rock':
                                rockCount += 1
                            if validChoices[w] == 'Paper':
                                paperCount += 1
                            if validChoices[w] == 'Scissors':
                                scissorsCount += 1
                            if validChoices[w] == 'quit':
                                quitCount += 1

                    # only entry with 1 non-zero choice is acceptable:
                    countNonZero = sum(var != 0 for var in [rockCount, paperCount, scissorsCount, quitCount])
                    if countNonZero - 1:
                        print('\"{}\" is not a valid choice. Please try again'.format(userEntry))
                        continue

                    # the entry is valid. let's see which one it is:
                    else:
                        if quitCount:  # Quit choice scenario
                            print('\n' + '+' * 62)
                            if not totalGameRounds:
                                print('Hope you play another time!')
                            else:
                                print('Thank you for playing this game. I really enjoyed it!')
                            print('+' * 62)
                            quit()

                        # the entry is not quit, and it's a game choice.
                        compChoice = random.choice(compChoicesTuple)
                        totalGameRounds += 1

                        # want to finalize userChoice from the userEntry:
                        if rockCount:
                            userChoice = 'rock'
                        elif paperCount:
                            userChoice = 'paper'
                        else:
                            userChoice = 'scissors'

                        # find the winner of current round:
                        print('\n' + '=' * 62)
                        if userChoice == compChoice:
                            print(tieMessage)
                        elif (userChoice == 'rock' and compChoice == 'scissors') or \
                                (userChoice == 'paper' and compChoice == 'rock') or \
                                (userChoice == 'scissors' and compChoice == 'paper'):
                            print(userWinMessage)
                            userWinCount += 1
                        else:
                            print(compWinMessage)
                            compWinCount += 1

                        print('I had: \"{}\" and your choice was: \"{}\"'.format(validChoices[compChoice],
                                                                                 validChoices[userChoice]))
                        print('=' * 62 + '\n')

                        print('Computer Score is : \'{}\''.format(compWinCount))
                        print('User Score is : \'{}\''.format(userWinCount))

                    # the condition of reaching winning score:
                    if userWinCount == winningScore or compWinCount == winningScore:
                        print('\n' + '*' * 62)
                        if userWinCount == winningScore:
                            print('Congratulations! Really good job, you won')
                        else:
                            print('Woohoo, I have won the game')
                        print('*' * 62)

                        while True:
                            proceedGame = input('\nDo you want to play again? (Y/N): ')
                            if proceedGame.lower() == 'n':
                                print('\n' + '+' * 62)
                                print('Hope you play this game another time :)')
                                print('+' * 62)
                                proceed = False
                                break

                            if proceedGame.lower() == 'y':
                                userWinCount = 0
                                compWinCount = 0
                                winningScore = 0
                                scoredRounds = 0
                                proceed = True
                                break
                        break
