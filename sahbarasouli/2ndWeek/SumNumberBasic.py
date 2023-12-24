def getIntFromStr(string1):
    resultS=0
    resultP=0
    finalRes=0
    dotindex=0
    percentpower=0
    for dotfinder in range (0,len(string1)):
         if(string1[dotfinder]=='.'):
            dotindex=dotfinder
            break
         else:
             dotindex=len(string1)

    if(string1[0]=='-' and string1[1]!=0):
       
        for i in range(1,dotindex):
            resultS= (-1)*(int)(string1[i])*10**(dotindex-1-i)+resultS
        for percentstring in range(dotindex+1,len(string1)):
            resultP= (-1)*(int)(string1[percentstring])*0.1**(percentstring-dotindex)+resultP
        finalRes=resultS+resultP

    else:
        for i in range(0,dotindex):
            resultS= (int)(string1[i])*10**(dotindex-1-i)+resultS
            
        for percentstring in range(dotindex+1,len(string1)):
            resultP= (int)(string1[percentstring])*0.1**(percentstring-dotindex)+resultP
        finalRes=resultS+resultP
    
    
    if(string1[0]=='-' and string1[1]==0):
          
        for percentstring in range(dotindex+1,len(string1)):
            resultP= (-1)*(int)(string1[percentstring])*0.1**(percentstring-dotindex)+resultP

            
        finalRes=resultP
    
    return finalRes
    
         
#################################   

str='15.62,-8.785,-0.25,125.12,-58,-0.23'
indx=0
sum=0
PNumer=0
templist=[]

while (indx<=str.__len__()):
    templist.clear()
    while (str[indx]!=','):
        templist.append(str[indx])
        indx=indx+1
        if(indx > str.__len__()-1):
            sum=getIntFromStr(templist)+sum
            break   
        
    indx=indx+1
    if(indx > str.__len__()-1):
            break
    sum=getIntFromStr(templist)+sum
print('the result is:{:.3f}'.format(sum) ) 
    