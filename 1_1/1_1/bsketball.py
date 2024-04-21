
yearly = int(input())

shoes = yearly - (yearly * 40 / 100)
clothes = shoes - (shoes * 20 / 100)
ball = clothes * 1 / 4
accessories = ball * 1 / 5

total = yearly + shoes + clothes + ball + accessories

print(total)
