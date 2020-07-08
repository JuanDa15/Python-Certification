largest = None
smallest = None
nums = []
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    else:
        try:
            Intscore = int(num)
        except:
            print("Invalid input")
            continue
        nums.append(int(num))

for i in nums:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i
    
    if largest is None:
        largest = i
    elif i > largest:
        largest = i

print("Maximum is", largest)
print("Minimum is", smallest)

#print("Maximum", largest)