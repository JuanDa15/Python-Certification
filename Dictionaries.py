filename = input("Enter Filename")

try:
    Document = open(filename,"r")
except:
    print("Document " + filename + "doesn exist")
    quit()


EmailDict = dict()

for line in Document:
    if line.startswith("From "):
        SplitedLine = line.split()
        EmailDict[SplitedLine[1]] = EmailDict.get(SplitedLine[1],0) + 1

bigCount = None
bigWord = None
for email,value in EmailDict.items():
    if bigCount is None or value > bigCount:
        bigCount = value
        bigWord = email
    

print (bigWord,bigCount)