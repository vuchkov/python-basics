import math

money = float(input())

leva = math.floor(money)
coins = math.floor((money - leva) * 100)
counter = 0

while leva > 0 or coins > 0:
    if leva >= 2:
        leva -= 2
    elif leva >= 1:
        leva -= 1
    elif leva == 0 and coins >= 50:
        coins -= 50
    elif leva == 0 and coins >= 20:
        coins -= 20
    elif leva == 0 and coins >= 10:
        coins -= 10
    elif leva == 0 and coins >= 5:
        coins -= 5
    elif leva == 0 and coins >= 2:
        coins -= 2
    elif leva == 0 and coins >= 1:
        coins -= 1
    counter += 1

print(counter)
