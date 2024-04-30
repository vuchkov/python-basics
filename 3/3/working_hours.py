hour = int(input())
day_of_the_week = input()

if 10 <= hour <= 18:
    if day_of_the_week == "Sunday":
        print("closed")
    else:
        print("open")
else:
    print("closed")
