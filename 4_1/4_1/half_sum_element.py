import sys

n = int(input())

sum_num = 0
max_num = -sys.maxsize
for _ in range(n):
    num = int(input())
    sum_num += num
    if max_num < num:
        max_num = num
diff = sum_num - max_num
if diff == max_num:
    print("Yes")
    print(f"Sum = {diff}")
else:
    print("No")
    print(f"Diff = {abs(diff - max_num)}")
