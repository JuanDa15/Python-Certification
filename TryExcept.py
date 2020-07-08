score = input("Enter Score: ")

try:
    Intscore = float(score)
except:
    print("Please enter a number")

if Intscore > 1.0:
    print ("Invalid score")
elif Intscore < 0.6:
    print("F")
elif (Intscore >= 0.6) and (Intscore < 0.7):
    print("D")
elif (Intscore >= 0.7) and (Intscore < 0.8):
    print("C")
elif (Intscore >= 0.8) and (Intscore < 0.9):
    print("B")
elif (Intscore >= 0.9) and (Intscore <= 1.0):
    print("A")