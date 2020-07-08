def computepay(hours,rate):
    if hours <= 40:
        pay = hours * rate
        return pay
    else:
        extraHours = hours - 40
        pay = (hours - extraHours) * rate
        payExtraHours = (extraHours * rate) * 1.5
        result = pay + payExtraHours
        return result


hours = int(input("Enter hours: "))
rate = float(input("Enter rate: "))

IntHours = 0
FloatRate = 0
try:
    IntHours = int(hours)
    FloatRate = float(rate)
except:
    print("Please enter valid information")


pay = computepay(IntHours,FloatRate)

print(pay)