hours = int(input("Enter hours: "))
rate = float(input("Enter rate: "))

pay = 0
if hours <= 40:
    pay = hours * rate
else:
    extraHours = hours - 40
    pay = (hours - extraHours) * rate
    payExtraHours = (extraHours * rate) * 1.5
    result = pay + payExtraHours


print(result)