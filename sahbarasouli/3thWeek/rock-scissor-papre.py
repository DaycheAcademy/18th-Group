import random


choices='paper','scissor','rock'
choiceforUser='paper','scissor','rock',' S ',' P ',' R ',' s ',' r ',' p ','p ',' p'
probablityWinCom=(('paper','rock','paper'),('scissor','paper','scissor'),('rock','scissor','rock'))
probablityWinUser=(('rock','paper','paper'),('paper','scissor','scissor'),('scissor','rock','rock'))
probablityEqual=(('rock','rock','equal'),('paper','paper','equal'),('scissor','scissor','equal'))

quitcheker=False
start=input('Are you ready to start?')
maxScore=input('do you want to the max scroe be?')
while( start=="y" or start=='yeah' or start=='yes'):
    cnt=0
    comCnt=0
    userCnt=0    
    if (not(maxScore.isdigit())):
        print('please set the correct value!!')
        maxScore=input('do you want to the max scroe be?')
    else:   
        while(cnt<int(maxScore)):
            if(quitcheker):
                 break
            tetsInp=True
            computerChoice=random.choice(choices)
            userChoice=input('choose which one?')
            
            while (tetsInp):
                    if('P' in userChoice or ' p ' in userChoice or 'paper' in userChoice or ' p' in userChoice  or 'p ' in userChoice or 'p' in userChoice):
                        userChoice='paper'
                        tetsInp=False
                    elif('R' in userChoice or ' r ' in userChoice or 'rock' in userChoice or 'r' in userChoice or ' r' in userChoice or 'r ' in userChoice):
                        userChoice='rock'
                        tetsInp=False
                    elif('S'in userChoice or ' s ' in userChoice or 'scissor' in userChoice or 's' in userChoice or ' s' in userChoice or 's ' in userChoice):
                        userChoice='scissor'
                        tetsInp=False
                    elif('Q'in userChoice or 'q' in userChoice or 'quit' in userChoice):
                         quitcheker=True
                         tetsInp=False
                         print('Thank you')
                         break
                    else:
                        print('please enter the correct input:')
                        userChoice=input('choose which one?') 
                    
            if userChoice in choices:
                    for iteratpr in probablityWinCom:
                        if iteratpr[0]==computerChoice and iteratpr[1]==userChoice:
                            comCnt+=1
                            print('computer Wins!!! \ncomputer choosed %s'%(computerChoice ))
                            print('computer\'s score is: %s ***** user\'s score is: %s'%(comCnt , userCnt))
                            print(45*'=')
                            break
                
                    for jtrator in probablityWinUser:
                        if(jtrator[0]==computerChoice and jtrator[1]==userChoice):
                            userCnt+=1
                            print('you Win!!! \ncomputer choosed %s'%(computerChoice))
                            print('computer\'s score is: %s ***** user\'s score is: %s'%(comCnt , userCnt))
                            print(45*'=')
                            break
                    for ktrator in probablityEqual:
                        if(ktrator[0]==computerChoice and ktrator[1]==userChoice):
                            print('its equal')
                            print('computer\'s score is: %s ***** user\'s score is: %s'%(comCnt , userCnt))
                            print(45*'=')
                            cnt-=1
        
            cnt+=1
        if(quitcheker):
             break
        if(userCnt>comCnt):
            print('you WIN!!!')
        else:
            print('you Lost')
        start=input('do u want to PLAY again?')
        if(start=='yes'):
            maxScore=input('do you want to the max scroe be?')
            continue
        else:
                break   