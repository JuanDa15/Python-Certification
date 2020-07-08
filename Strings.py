"""Document = open('test.txt','r')

for line in Document:
    if line.startswith("From: "):
        newline = line.rstrip()
        print (newline)
 """ 
lines = 0
floatNumber = 0
filename = input("Enter FileName with .txt: ")
try:
    document = open(filename)
except:
    print("File " + filename + " Doesnt exist")
    quit()

for line in document:
    if line.startswith("X-DSPAM-Confidence: "):
        lines += 1
        #Option 1
        #position = line.find(":")
        #floatNumber += float(line[position + 1:])
        #Option 2
        lists = line.split()
        floatNumber += float(lists[1])
        
average = floatNumber/lines
print("Average spam confidence:",average)

#test
