import sys

min_n = sys.maxsize
max_n = -sys.maxsize

n = int(input())

for i in range(n):
    temp = int(input())
    if temp < min_n:
        min_n = temp
    if temp > max_n:
        max_n = temp

print(f"Max number: {max_n}")
print(f"Min number: {min_n}")
