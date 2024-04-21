BONUS_1 = 5
BONUS_100 = 20 / 100
BONUS_1000 = 10 / 100
BONUS_EVEN = 1
BONUS_5 = 2

i = int(input())

p = i
if i <= 100:
    p += BONUS_1
elif i <= 1000:
    p += i * BONUS_100
else:
    p += i * BONUS_1000

if i % 2 == 0:
    p = p + BONUS_EVEN
elif i % 5 == 0:
    p = p + BONUS_5

bonus = p - i
print(f"{bonus:0.1f}")
print(f"{p:0.1f}")
