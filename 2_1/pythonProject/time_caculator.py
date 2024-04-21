hours = int(input())
minutes = int(input())

next_minutes = minutes + 15
next_hours = hours
if next_minutes >= 60:
    next_hours = hours + 1
    next_minutes = next_minutes - 60
if next_hours == 24:
    next_hours = next_hours - 24

print(f"{next_hours}:{next_minutes:02d}")
