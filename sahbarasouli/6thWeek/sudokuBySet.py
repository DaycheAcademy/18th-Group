import turtle
import random
#Function1:creating Valid set for each positionL
def setSqurefiller(i,j):
    rowSet=set()
    colSet=set()
    result=set()
    squareSet=set()
    myChoice={1,2,3,4,5,6,7,8,9}
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
    res=sorted(result, key=lambda x: random.random())
    return res

#Function2:filling sudoku 
def fillsudo(myBoard):
  
    for i in range(9):   
        for j in range(9):
            if myBoard[i][j]==0:
                for k in setSqurefiller(i,j): 
                     myBoard[i][j]=k            
                     if fillsudo(myBoard):
                        return True
                     myBoard[i][j] = 0    
                return  False                       
    return True

if __name__=='__main__':

    #DrAWING
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
    temprList=list()
    tempcList=list()
    finalListRow=list()
    finalListCol=list()
    mySudoku.penup()

   #execution: 
    finalList=[[0 for _ in range(9)]  for _ in range(9)]
    fillsudo(finalList)
    for row in  range (0,9):
        for col in range (0,9):
            mySudoku.goto(-195+col*50,195-row*50)
            mySudoku.write(finalList[row][col])

    turtle.done()


