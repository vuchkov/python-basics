CHICKEN = 10.35
FISH = 12.40
VEGAN = 8.15
DESERT = 20 / 100
DELIVERY = 2.50

chicken = int(input())
fish = int(input())
vegan = int(input())

all_chicken = chicken * CHICKEN
all_fish = fish * FISH
all_vegan = vegan * VEGAN
all = all_chicken + all_fish + all_vegan
all_desert = all * DESERT

total = all + all_desert + DELIVERY

print(total)
