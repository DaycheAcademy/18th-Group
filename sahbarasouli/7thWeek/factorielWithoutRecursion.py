#Func of factorial without recursion(just by current and previous)
def factorial(n):
    current=1
    for i in range(1,n+1):  
        current=current*i
    return current

#Func of RangeOfFloat by generator
def rangeGenerator(start,stop,step):
    while start<=stop:
        yield start 
        start=start+step

        
#Func of ALphabetGenerator without Range
def alphaGenerator(start:str,stop:str,step):
    str=list('abcdefghijklmnopqrttuvwxyz')
    startVal=str.index(start.lower())
    while startVal <= str.index(stop.lower()):
        yield str[startVal]
        startVal=startVal+step


if __name__ == '__main__':    
    #factorial without recursion(just by current and previous)
    print(f'the factorial of 5 is :{factorial(5)}')

    print('*'*50)

    #float generator
    for j in rangeGenerator(2.4,3.6,0.01):
         print(('{0:.2f}'.format(j)))

    print('*'*50)

    # Alphabet Generator
    for w in alphaGenerator('R','z',3):
         print(w)
