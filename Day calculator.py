
print("Welcome to the day calculator, made by Akshaj Keshav! Let's get started!")


udate = int(input("Enter date: "))
umonth = int(input("Enter month (1-12): "))
uyr = int(input("Enter year: "))


days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


daysm = sum(days_in_month[:umonth - 1])

specialleap = 0
if (uyr % 4 == 0 and uyr % 100 != 0) or uyr % 400 == 0:
    specialleap = 1


ly = uyr // 4
lyd = uyr // 100
lyi = uyr // 400
finallyr = ly + lyi - lyd
finaly = 365 * uyr + finallyr - specialleap


nodays = finaly + daysm + udate - 1

x = nodays % 7

if x == 0:
    print("Monday")
elif x == 1:
    print("Tuesday")
elif x == 2:
    print("Wednesday")
elif x == 3:
    print("Thursday")
elif x == 4:
    print("Friday")
elif x == 5:
    print("Saturday")
else:
    print("Sunday")
