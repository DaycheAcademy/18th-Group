cnt=0
sum=0
calc_Mean=0
while True:
     enternumber=input('enter number:')
     if (enternumber.lower()=='q'or enternumber.lower()=='quit'):
          break
     if(not enternumber.isdigit()):
        continue
     else :
          sum=((int)(enternumber))+sum     
          cnt+=1
          calc_Mean=sum/cnt
     
     
    
     
print(calc_Mean)

