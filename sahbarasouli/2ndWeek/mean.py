
cnt=1
sum=0
enternumber=0
enternumber=input('enter number:')
while True:
    if(enternumber!='q'):
        try:
            
            sum=((int)(enternumber))+sum
            calc_Mean=sum/cnt
            cnt+=1
            enternumber=input('enter number:')
            
        except ValueError:
            print('thas not correct!')
            enternumber=input('enter number:')
           

    else:
        break
print((calc_Mean*100)/100)
        