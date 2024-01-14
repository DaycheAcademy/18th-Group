import turtle
import random

#Function(1) cerate valid set for each position(i,j) and put it into the dictionary{(key):{values}} :
def setChecker(i,j):
    rowSet=set()
    colSet=set()
    result=set()
    myChoice={1,2,3,4,5,6,7,8,9}
    squareSet=set()

    for mover1 in range(9): 
            rowSet.add(finalList[i][mover1])
    rowSet.remove(finalList[i][j])

    for mover2 in range(9): 
            colSet.add(finalList[mover2][j])
    colSet.remove(finalList[i][j])

    for r in range((i//3)*3,((i//3)+1)*3):
        for c in range((j//3)*3,((j//3)+1)*3):
                squareSet.add(finalList[r][c])

    result=((myChoice-rowSet)-colSet)-squareSet
    x=sorted(result, key=lambda x: random.random())
    mydict={(i,j):x}
    return mydict

#Function(2):solving sufoku by using Function(1) and 2 global varriables instead of for :

def fillsudo():  
    global first,second,dict
    dict=setChecker(first,second)

    if finalList[first][second]==0:
        for u in dict.get((first,second)): 
            finalList[first][second]=u
            second+=1
            
            if first<8 and second>8:
                first+=1
                second=0
            
            elif first==8 and second>8:                     
                return True           
            
            if fillsudo():
                return True
            finalList[first][second] = 0   
            if second>0:
                second-=1
            else:
                second=8
                first-=1
        return  False
                     
    return True

if __name__ =='__main__' :

    #DrAWING:
    mySudoku=turtle.Turtle(visible=False)
    mySudoku.clear()
    mySudoku.penup()
    mySudoku.speed(0)

    for i in range(10):
        if i == 0 or i == 9:
            mySudoku.pensize(5)
        elif i % 3 ==0 :
            mySudoku.pensize(3)
        else:
            mySudoku.pensize(1)
        mySudoku.penup()
        mySudoku.goto(-220+50*i,220)
        mySudoku.pendown()
        mySudoku.right(90)
        mySudoku.forward(450)

        mySudoku.penup()
        mySudoku.goto(-220,220-50*i)
        mySudoku.pendown()
        mySudoku.left(90)
        mySudoku.forward(450)
    mySudoku.penup()  

    finalList=list()
    tempList=list()
    mydict={}
    dict={}
    first=0
    second=0

# execution:
    finalList=[[0 for _  in range(9)] for _ in range(9)]
    fillsudo()
          
    for row in  range (0,9):
        for col in range (0,9):
            mySudoku.goto(-195+col*50,195-row*50)
            mySudoku.write(finalList[row][col])

    turtle.done()


