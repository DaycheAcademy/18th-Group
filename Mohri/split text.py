UserName = []
Identifier = []
FirstName = []
LastName = []

#Open the file for reading
with open('file-csv.txt', 'r') as fileScv:
  FileText = fileScv.readline().strip('\n')

#Adds each part to its list
  while FileText:
   FileText = FileText.split(';')
   UserName.append(FileText[0])
   UserName.append(",")
   Identifier.append(FileText[1])
   Identifier.append(",")
   FirstName.append(FileText[2])
   FirstName.append(",")
   LastName.append(FileText[3])
   LastName.append(",")
   FileText = fileScv.readline().strip('\n')

#write each part in it file
with open('file-csv.txt', 'wt') as fileScv:
 fileScv.writelines("UserName: ")
 fileScv.writelines(UserName)
 fileScv.writelines("\n")
 fileScv.writelines("Identifier: ")
 fileScv.writelines(Identifier)
 fileScv.writelines("\n")
 fileScv.writelines("FirstName: ")
 fileScv.writelines(FirstName)
 fileScv.writelines("\n")
 fileScv.writelines("LastName: ")
 fileScv.writelines(LastName)
 fileScv.writelines("\n")
