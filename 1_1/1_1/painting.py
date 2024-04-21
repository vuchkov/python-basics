nylon = 1.50
paint = 14.50
acetone = 5.00

percent = 10 / 100
nylon_plus = 2
bags = 0.40

working_hour = 30 / 100

p1 = int(input())
p2 = int(input())
p3 = int(input())
p4 = int(input())

all_nylon = (p1 + nylon_plus) * nylon
all_paint = (p2 + (p2 * percent)) * paint
all_acetone = p3 * acetone

materials = all_nylon + all_paint + all_acetone + bags
worker = materials * working_hour * p4
total = materials + worker

print(total)
