         
for num in range(2,100):
        for calc in range(2,num//2+1):
                if(not num%calc):
                        break
        else:
            print(num)