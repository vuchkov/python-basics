fruit = input()
day_of_the_week = input()
quantity = float(input())
price = 0.0

if day_of_the_week == "Monday" or day_of_the_week == "Tuesday" or day_of_the_week == "Wednesday" or day_of_the_week == "Thursday" or day_of_the_week == "Friday":
    if fruit == "banana": price = quantity * 2.5
    elif fruit == "apple": price = quantity * 1.2
    elif fruit == "orange": price = quantity * 0.85
    elif fruit == "grapefruit": price = quantity * 1.45
    elif fruit == "kiwi": price = quantity * 2.70
    elif fruit == "pineapple": price = quantity * 5.50
    elif fruit == "grapes": price = quantity * 3.85
elif day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
    if fruit == "banana":
        price = quantity * 2.7
    elif fruit == "apple":
        price = quantity * 1.25
    elif fruit == "orange":
        price = quantity * 0.90
    elif fruit == "grapefruit":
        price = quantity * 1.60
    elif fruit == "kiwi":
        price = quantity * 3.00
    elif fruit == "pineapple":
        price = quantity * 5.60
    elif fruit == "grapes":
        price = quantity * 4.20

if price > 0:
    print(f"{price:0.2f}")
else:
    print("error")

