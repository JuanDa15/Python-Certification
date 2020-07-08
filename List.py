filename = input("Enter filename with .txt: ")
try:
    Document = open(filename,"r")
except:
    print("Incorrect filename")
    quit()

words = list()
for line in Document:
    SplitedLine = line.split()
    for i in range(len(SplitedLine)):
        if SplitedLine[i] in words:
            continue
        else:
            words.append(SplitedLine[i])

words.sort()
print(words)

#test 2