
x = int(input())
y = int(input())
z = int(input())
percent = float(input()) / 100

liters = x * y * z / 1000
total = liters - (liters * percent)

print(total)