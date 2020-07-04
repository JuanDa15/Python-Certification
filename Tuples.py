#ORDER WORDS WITH TUPLES
Filename = input("Enter File name: ")
try:
    Document = open(Filename,"r")
except:
    print("Document" + Filename + "Doesnt exist")
#Hours list
HoursList = list()

for line in Document:
    if line.startswith("From "):
        SplitedLine = line.split()
        RecortedHour = SplitedLine[5]
        HoursList.append(RecortedHour.split(":")[0])

Dictionary = dict()
for Hour in HoursList:
    Dictionary[Hour] = Dictionary.get(Hour,0) + 1

HoursList2 = list()
for key,value in Dictionary.items():
    NewItem = (key,value)
    HoursList2.append(NewItem)
    
for key,value in sorted(HoursList2):
    print(key,value)