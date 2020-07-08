import re

filename = input("Enter filename: ")
try:
    Document = open(filename,"r")
except:
    print("Error file " + filename + "Doesnt exist")
    quit()
FinalList= list()
result = 0
for line in Document:
    EditedLine = line.strip()
    Numbers = re.findall('([0-9]*)',EditedLine)
    for Number in Numbers:
        if Number != '':
            FinalList.append(int(Number))
            
    result = sum(FinalList)


print(result)