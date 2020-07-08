
filename = input("Enter filename: ")
try:
    Document = open(filename,"r")
except:
    print("File " + filename + " Doesnt exist")
    quit()

count = 0
for line in Document:
    if line.startswith("From "):
        SplitedLine = line.split()
        count += 1
        print (SplitedLine[1])


print("There were", count, "lines in the file with From as the first word")