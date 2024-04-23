VIDEO = 250
CPU = 35 / 100
RAM = 10 / 100
DISCOUNT = 15 / 100

budget = float(input())
videos = int(input())
cpus = int(input())
rams = int(input())

total_videos = videos * VIDEO
total = total_videos
total += cpus * total_videos * CPU
total += rams * total_videos * RAM

if videos > cpus:
    total -= total * DISCOUNT

if total <= budget:
    total = budget - total
    print(f"You have {total:.2f} leva left!")
else:
    total -= budget
    print(f"Not enough money! You need {total:.2f} leva more!")
