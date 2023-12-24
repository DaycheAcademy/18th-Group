import random
gameChoice = "Paper", "Rock", "Scissor"
WinningScores = 0
inputWinning = True
UserChoiceMain = ""
# ====================================================================================
probabilityWinCom = (('Paper', 'Rock', 'Paper'), ('Scissor', 'Paper', 'Scissor'), ('Rock', 'Scissor', 'Rock'))
probabilityWinUser = (('Rock', 'Paper', 'Paper'), ('Paper', 'Scissor', 'Scissor'), ('Scissor', 'Rock', 'Rock'))
probabilityEqual = (('Rock', 'Rock', 'Equal'), ('Paper', 'Paper', 'Equal'), ('Scissor', 'Scissor', 'Equal'))
# ====================================================================================
validChoiceRock = {"Rock": "R",
                   "rock": "r",
                   "ROCK": "ROCK"
                   }
gameSetRock = set(validChoiceRock.keys())
gameSetRock = gameSetRock.union(validChoiceRock.values())
# ------------------------------------------------
validChoiceScissors = {"Scissor": "S",
                       "s": "scissor",
                       "SCISSOR": "SCISSOR"
                       }
gameSetScissors = set(validChoiceScissors.keys())
gameSetScissors = gameSetScissors.union(validChoiceScissors.values())
# ------------------------------------------------
validChoicePaper = {"Paper": "P",
                    "paper": "p",
                    "PAPER": "PAPER"
                    }
gameSetPaper = set(validChoicePaper.keys())
gameSetPaper = gameSetPaper.union(validChoicePaper.values())
# ====================================================================================
validChoiceQuit = {"q": "quit",
              "Q": "Quit",
              "QUIT": "QUIT"
              }
gameSetQuit = set(validChoiceQuit.keys())
gameSetQuit = gameSetQuit.union(validChoiceQuit.values())
# ====================================================================================
validChoiceYes = {"y": "yes",
              "Y": "Yes",
              "YES": "YES"
              }
gameSetYes = set(validChoiceYes.keys())
gameSetYes = gameSetYes.union(validChoiceYes.values())
# ====================================================================================

while inputWinning:
    print()
    print("****************** :) I am very happy because you want to play with me (: ******************")
    print()
    WinningScore = input("How much do we play together?(type quit to end):").strip()
    print()
    if gameSetQuit.intersection(WinningScore):
        UserQuit = input("              Do you want to quit ?(YES or NO) ").split(sep=' ')
        print()
        if gameSetYes.intersection(UserQuit):
            print("*** Thanks for spend time with me ***")
            print()
            inputWinning = False
            quit()
        else:
            print()
    if WinningScore.isdigit():
        print("                             ********** Let's Go... **********")
        print()
        Count = True
        Counter = 0
        compWinCount = 0
        userWinCount = 0
        WinningScores = int(WinningScore)
        while Count:
            if Counter < WinningScores:
                UserChoice = input("Please write choice(Paper, Rock, Scissors, Quit):").split(sep=' ')
                print()
                compChoice = random.choice(gameChoice)
                if gameSetQuit.intersection(UserChoice):
                   UserQuit = input("              Do you want to quit ?(YES or NO)").split(sep=' ')
                   print()
                   if gameSetYes.intersection(UserQuit):
                    print("*** Thanks for spend time with me ***")
                    print()
                    inputWinning = False
                    quit()
                   else:
                    print()
                elif gameSetRock.intersection(UserChoice):
                    Counter += 1
                    UserChoiceMain = "Rock"
                elif gameSetPaper.intersection(UserChoice):
                    Counter += 1
                    UserChoiceMain = "Paper"
                elif gameSetScissors.intersection(UserChoice):
                    Counter += 1
                    UserChoiceMain = "Scissors"
                for iterator in probabilityWinCom:
                    if iterator[0] == compChoice and iterator[1] == UserChoiceMain:
                        compWinCount += 1
                        print("-" * 69)
                        print("     Your choice is:", UserChoiceMain, "      My choice is:", compChoice)
                        print("                :) I win Horaaaaaaaaaaaaaaa")
                        print('                 I score {} and YOU score {}'.format(compWinCount, userWinCount))
                        print("-" * 69)
                        break
                for iterator in probabilityWinUser:
                    if iterator[0] == compChoice and iterator[1] == UserChoiceMain:
                        userWinCount += 1
                        print("-" * 69)
                        print("     Your choice is:", UserChoiceMain, "      My choice is:", compChoice)
                        print("                    :( YOU win")
                        print('             I score {} and YOU score {}'.format(compWinCount, userWinCount))
                        print("-" * 69)
                        break
                for iterator in probabilityEqual:
                    if iterator[0] == compChoice and iterator[1] == UserChoiceMain:
                        print("-" * 69)
                        print("     Your choice is:", UserChoiceMain, "      My choice is:", compChoice,)
                        print("                   :| We are equal")
                        print('               I score {} and YOU score {}'.format(compWinCount, userWinCount))
                        print("-" * 69)
                        break
            else:
                Count = False
        UserQuit = input("              Do you want to quit ?(YES or NO) ").split(sep=' ')
        print()
        if gameSetYes.intersection(UserQuit):
            print("*** Thanks for spend time with me ***")
            print()
            inputWinning = False
            quit()
        else:
            print()




