import random

computerChoice = ("rock", "paper", "scissor")
userChoiceStart_No = {"no", "n"}
userChoiceStart_Yes = {"yes", "y"}
userChoiceQuit = {"q", "quit"}
userChoiceRock = {"r", "rock"}
userChoicePaper = {"p", "paper"}
userChoiceScissor = {"s", "scissor"}
userAllValidChoices = userChoiceQuit.union(userChoiceStart_Yes, userChoiceStart_No,
                                           userChoiceRock, userChoicePaper, userChoiceScissor)
print(" * " * 30)
print("----------------------I AM VERY HAPPY THAT YOU WANT PLAY TOGETHER--------------------------")
print(" * " * 30)

startGame = True
while startGame:
    firstUserRequest = input(" Do you want to play:[Yes / No] ??  [q / quit] for exit    ").strip().lower().split(" ")
    print(" * " * 15)
    print(" * " * 15)
    print(" * " * 15)

    if set(firstUserRequest).intersection(userChoiceStart_No):
        print("---------I'm glad you entered this game---------")

    elif set(firstUserRequest).intersection(userChoiceQuit):
        print("---- Come joins us again -----")
        quit()

    elif set(firstUserRequest).intersection(userChoiceStart_Yes):
        print("----------------OK Let's go-------------------")
        print(" * " * 15)
        print(" * " * 15)
        print(" * " * 15)

        firstStartGame = True
        while firstStartGame:
            secondUserRequest = input("How many rounds should we play? ([q / quit] for exit) :      ")
            print(" * " * 15)

            if set(secondUserRequest.strip().lower().split(" ")).intersection(userChoiceQuit):
                print("---- Come joins us again -----")
                quit()

            elif secondUserRequest.isdigit():
                print(f"You chose to play {secondUserRequest} rounds")
                print("* " * 15)
                print("* " * 15)

                scoreComputer = 0
                scoreUser = 0
                countGame = 0
                countGameUser = int(secondUserRequest)
                secondStartGame = True

                while secondStartGame:

                    if countGameUser > countGame:
                        comChoice = random.choice(computerChoice)
                        tripleUserRequest = input("Choose one of the : rock/paper/scissor ???[q / quit] for exit !!)  ")
                        countGame += 1

                        if set(tripleUserRequest.strip().lower().split(" ")).intersection(userChoiceQuit):
                            print("---- Come joins us again -----")
                            secondStartGame = False
                            quit()

                        elif set(tripleUserRequest.strip().lower().split(" ")).intersection(userChoiceRock):
                            userChoice = "rock"
                            print(
                                "In round {} of game, i chose {} and you {} ".format(countGame, comChoice, userChoice))

                            if comChoice == "paper":
                                scoreComputer += 1

                            elif comChoice == "rock":
                                countGame -= 1
                                print("----Well , nothing this time----")

                            else:
                                scoreUser += 1
                            print("My score so far is {} and your score is {}".format(scoreComputer, scoreUser))
                            print("-" * 15)
                            print("-" * 15)
                            print("-" * 15)

                        elif set(tripleUserRequest.strip().lower().split(" ")).intersection(userChoicePaper):
                            userChoice = "paper"
                            print("In round {} of game,i chose {} and you {} ".format(countGame, comChoice, userChoice))

                            if comChoice == "scissor":
                                scoreComputer += 1

                            elif comChoice == "paper":
                                print("----Well , nothing this time----")

                            else:
                                scoreUser += 1
                            print("My score so far is {} and your score is {}".format(scoreComputer, scoreUser))
                            print("-" * 15)
                            print("-" * 15)
                            print("-" * 15)

                        elif set(tripleUserRequest.strip().lower().split(" ")).intersection(userChoiceScissor):
                            userChoice = "scissor"
                            print(
                                "In round {} of game, i chose {} and you  {} ".format(countGame, comChoice, userChoice))

                            if comChoice == "rock":
                                scoreComputer += 1

                            elif comChoice == "scissor":
                                countGame -= 1
                                print("----Well , nothing this time----")

                            else:
                                scoreUser += 1
                            print("My score so far is {} and your score is {}".format(scoreComputer, scoreUser))
                            print("-" * 15)
                            print("-" * 15)
                            print("-" * 15)
                        else:
                            print("I didn't understand, please choose again")
                            countGame -= 1

                    elif countGameUser <= countGame:

                        if scoreComputer > scoreUser:
                            print("-----------------YOU LOSS---------------- ")
                            secondStartGame = False
                            firstStartGame = False

                        elif scoreComputer < scoreUser:
                            print("-----------------YOU WON----------------- ")
                            secondStartGame = False
                            firstStartGame = False
            else:
                print("I didn't understand, please try again")

    else:
        print("I didn't understand, please try again")
