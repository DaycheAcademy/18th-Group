code=[]
symboll=[]
name=[]
with open('D:\Sahbaa\MyDataSience\python\Dayche\18th-Group\sahbarasouli\ 5thWeek\color.txt','r') as handFile:
    lines=handFile.readline()
    
    while(lines):
        wordOfEachLin=lines.split(',')
        code.append(wordOfEachLin[0])
        symboll.append(wordOfEachLin[1])
        name.append(wordOfEachLin[2].strip('\n'))
        code.append('\t')
        symboll.append('\t')
        name.append('\t')
        lines=handFile.readline()
with  open ('D:\Sahbaa\MyDataSience\python\Dayche\ 18th-Group\sahbarasouli\ 5thWeek\ result.txt','wt') as handFile:  
    handFile.writelines((code))
    handFile.writelines('\n')
    handFile.writelines(symboll)
    handFile.writelines('\n')
    handFile.writelines(name)
