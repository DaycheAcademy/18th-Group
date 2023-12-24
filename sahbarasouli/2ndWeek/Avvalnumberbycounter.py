cnt=0
for num1 in range(2,1000):
    for calc1 in range (2,num1):
        if( not num1%calc1):
            cnt+=1
            break
    else:
        print(num1)
        # else:
        #     continue

    # if(cnt==0):
    #     print(num1)
    # cnt=0
