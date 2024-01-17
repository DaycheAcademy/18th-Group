import random


def getscore(choice1, choice2):
    global countGame
    global scoreUser
    global scoreComputer
    if choice1 == choice2:
        countGame -= 1
        print("----Well , nothing this time----")

    elif set(choice1.lower()).intersection(userChoiceRock):
        if set(choice2.lower()).intersection(userChoiceScissor):
            scoreUser += 1
        else:
            scoreComputer += 1
    elif set(choice1.lower()).intersection(userChoiceScissor):
        if set(choice2.lower()).intersection(userChoicePaper):
            scoreUser += 1
        else:
            scoreComputer += 1
    elif set(choice1.lower()).intersection(userChoicePaper):
        if set(choice2.lower()).intersection(userChoiceRock):
            scoreUser += 1
        else:
            scoreComputer += 1

    return countGame, scoreUser, scoreComputer


if __name__ == "__main__":

    computerChoice = ("rock", "paper", "scissor")
    userChoiceStart_No = {"no", "n"}
    userChoiceStart_Yes = {"yes", "y"}
    userChoiceQuit = {"q", "quit"}
    userChoiceRock = {"r", "rock"}
    userChoicePaper = {"p", "paper"}
    userChoiceScissor = {"s", "scissor"}
    print(" * " * 15)
    print("------------------I AM VERY HAPPY THAT YOU WANT PLAY TOGETHER----------------------")
    print(" * " * 15)

    startGame = True
    while startGame:
        firstUserRequest = input(" Do you want to play:(Yes / No)    ").strip().lower().split(" ")
        print(" * " * 15)
        print(" * " * 15)
        print(" * " * 15)

        if set(firstUserRequest).intersection(userChoiceStart_No):
            print("I'm glad you entered this game, lets play another time. press q/quit for exit")

        elif set(firstUserRequest).intersection(userChoiceQuit):
            print("---- Come joins us again -----")
            quit()

        elif set(firstUserRequest).intersection(userChoiceStart_Yes):
            print("----------------OK Let's go-------------------")
            print(" * " * 30)
            print(" * " * 30)

            firstStartGame = True
            while firstStartGame:
                secondUserRequest = input("How many rounds should we play?(press q/quit for exit) :      ")
                print(" * " * 30)

                if set(secondUserRequest.strip().lower().split(" ")).intersection(userChoiceQuit):
                    print("---- Come joins us again -----")
                    quit()

                elif secondUserRequest.isdigit():
                    print(f"You chose to play {secondUserRequest} rounds")
                    print("* " * 30)
                    print("* " * 30)

                    scoreComputer = 0
                    scoreUser = 0
                    countGame = 0
                    countGameUser = int(secondUserRequest)
                    secondStartGame = True

                    while secondStartGame:

                        if countGameUser > countGame:
                            comChoice = random.choice(computerChoice)
                            tripleUserRequest = input(
                                "Choose one of the : rock/paper/scissor (press q/quit for exit !!): ")
                            countGame += 1

                            if set(tripleUserRequest.strip().lower().split(" ")).intersection(userChoiceQuit):
                                print("---- Come joins us again -----")
                                secondStartGame = False
                                quit()

                            elif set(tripleUserRequest.strip().lower().split(" ")).intersection(userChoiceRock):
                                userChoice = "rock"
                                print("In round {} of game, i chose {} and you {} ".format(countGame, comChoice,
                                                                                           userChoice))
                                getscore(userChoice, comChoice)
                                print("My score so far is {} and your score is {}".format(scoreComputer, scoreUser))
                                print("-" * 30)
                                print("-" * 30)
                                print("-" * 30)

                            elif set(tripleUserRequest.strip().lower().split(" ")).intersection(userChoicePaper):
                                userChoice = "paper"
                                print("In round {} of game,i chose {} and you {} ".format(countGame, comChoice,
                                                                                          userChoice))

                                getscore(userChoice, comChoice)
                                print("My score so far is {} and your score is {}".format(scoreComputer, scoreUser))
                                print("-" * 30)
                                print("-" * 30)
                                print("-" * 30)

                            elif set(tripleUserRequest.strip().lower().split(" ")).intersection(userChoiceScissor):
                                userChoice = "scissor"
                                print("In round {} of game, i chose {} and you  {} ".format(countGame, comChoice,
                                                                                            userChoice))

                                getscore(userChoice, comChoice)
                                print("My score so far is {} and your score is {}".format(scoreComputer, scoreUser))
                                print("-" * 30)
                                print("-" * 30)
                                print("-" * 30)
                            else:
                                print("I didn't understand, please choose again")
                                countGame -= 1
                        elif countGameUser <= countGame:

                            if scoreComputer > scoreUser:
                                print("-----------------YOU LOST---------------- ")
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
