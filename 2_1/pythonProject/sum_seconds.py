first = int(input())
second = int(input())
third = int(input())

sum = first + second + third

min = sum // 60
sec = sum % 60

# if sec < 10:
#     print(f"{min}:0{sec}")
# else:
#     print(f"{min}:{sec}")

print(f"{min}:{sec:02d}")
