even_sum = 0
odd_sum = 0

n = int(input())

for i in range(n):
    t = int(input())
    if i == 0 or i % 2 == 0:
        even_sum += t
    else:
        odd_sum += t

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    if even_sum > odd_sum:
        diff = even_sum - odd_sum
    else:
        diff = odd_sum - even_sum
    print(f"No")
    print(f"Diff = {diff}")
