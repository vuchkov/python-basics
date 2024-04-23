import math

SLOW_15M = 12.5

record = float(input())
meters = float(input())
time = float(input())

time_to_swim = meters * time
slow = math.floor(meters / 15) * SLOW_15M
time_to_swim += slow

if time_to_swim < record:
    print(f"Yes, he succeeded! The new world record is {time_to_swim:.2f} seconds.")
else:
    time_to_swim -= record
    print(f"No, he failed! He was {time_to_swim:.2f} seconds slower.")
