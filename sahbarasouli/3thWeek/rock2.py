import random
choices='paper','scissor','rock'
probablityWinCom=(('paper','rock','paper'),('scissor','paper','scissor'),('rock','scissor','rock'))
probablityWinUser=(('rock','paper','paper'),('paper','scissor','scissor'),('scissor','rock','rock'))
probablityEqual=(('rock','rock','equal'),('paper','paper','equal'),('scissor','scissor','equal'))
probablity=((('paper','rock','paper'),('scissor','paper','scissor'),('rock','scissor','rock')),(('paper','scissor','scissor'),('rock','paper','paper'),('rock','scissor','rock')),
 (('rock','rock','equal'),('paper','paper','equal'),('scissor','scissor','equal')))

maxScore=input('do you want to the max scroe be?')
cnt=0
comCnt=0
userCnt=0
while(cnt<int(maxScore)):
    tetsInp=True
    computerChoice=random.choice(choices)
    userChoice=input('choose which one?')
    while (tetsInp):
            if(' P ' in userChoice or ' p ' in userChoice or 'paper' in userChoice):
                userChoice='paper'
                tetsInp=False
                cnt+=1
            elif(' R ' in userChoice or ' r ' in userChoice or 'rock' in userChoice):
                userChoice='rock'
                tetsInp=False
                cnt+=1
            elif(' S 'in userChoice or ' s ' in userChoice or 'scissor' in userChoice):
                userChoice='scissor'
                tetsInp=False
                cnt+=1
            else:
                print('please enter the correct input:')
                userChoice=input('choose which one?')
            newtuple=(computerChoice,userChoice)
            matchTest=0
            loopMngr=True
            for prbcheking in probablity:
                for row in range(0,2):
                    matchTest=0
                    for col in range(0,2):
                        if prbcheking[row][col]==newtuple[col]:
                            matchTest+=1
                            if(matchTest==2):
                                
                                if newtuple[0]==prbcheking[row][2]:
                                    print('computer wins and it  choosed %s'%((newtuple[0] )))
                                    comCnt+=1
                                    loopMngr=False
                                    break
                                elif newtuple[1]==prbcheking[row][2]:
                                    print('user wins and computer  choosed %s'%((newtuple[0] )))
                                    userCnt=+1
                                    loopMngr=False
                                    break
                                else:
                                    print('equal')
                                    cnt-=1
                                    loopMngr=False
                                    break
                if(not loopMngr):
                    break
            if (not loopMngr):
                break
                            
    