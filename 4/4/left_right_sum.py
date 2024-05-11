left_sum = 0
right_sum = 0

n = int(input())

for i in range(n):
    left_sum += int(input())
for i in range(n):
    right_sum += int(input())
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    if left_sum > right_sum:
        diff = left_sum - right_sum
    else:
        diff = right_sum - left_sum
    print(f"No, diff = {diff}")
