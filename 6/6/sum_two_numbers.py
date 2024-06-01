x1 = int(input()) # 1..999
x2 = int(input()) # x2 > x1
magic_number = int(input()) # 1..10000

counter = 0
found = 0
for i in range(x1, x2 + 1):
    for j in range(x1, x2 + 1):
        counter += 1
        if i + j == magic_number:
            if found == 0:
                print(f"Combination N:{counter} ({i} + {j} = {i + j})")
                found = 1
if found == 0:
    print(f"{counter} combinations - neither equals {magic_number}")
