import sys

s = input()
min_number = sys.maxsize

while s != "Stop":
    number = int(s)
    if min_number > number:
        min_number = number
    s = input()

print(min_number)
