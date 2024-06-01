hour = 0
minutes = 0

while hour < 24 and minutes < 60:
    print(f"{hour}:{minutes}")
    minutes += 1
    if minutes == 60 and hour < 24:
        minutes = 0
        hour += 1
