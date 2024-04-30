ROSES = "Roses"
DAHLIAS = "Dahlias"
TULIPS = "Tulips"
NARCISSUS = "Narcissus"
GLADIOLUS = "Gladiolus"

ROSE = 5
DALIA = 3.80
LALE = 2.80
NARCIS = 3
GLADIOLA = 2.50

ROSES_COUNT = 80
ROSES_RATE = 10 / 100
DAHLIAS_COUNT = 90
DAHLIAS_RATE = 15 / 100
TULIPS_COUNT = 80
TULIPS_RATE = 15 / 100

NARCISSUS_COUNT = 120
NARCISSUS_RATE = 15 / 100
GLADIOLUS_COUNT = 80
GLADIOLUS_RATE = 20 / 100

flower_type = input().strip()
flower_count = int(input())
budget = int(input())

price = 0
if flower_type == ROSES:
    price = flower_count * ROSE
    if flower_count > ROSES_COUNT:
        price -= price * ROSES_RATE
elif flower_type == DAHLIAS:
    price = flower_count * DALIA
    if flower_count > DAHLIAS_COUNT:
        price -= price * DAHLIAS_RATE
elif flower_type == TULIPS:
    price = flower_count * LALE
    if flower_count > TULIPS_COUNT:
        price -= price * TULIPS_RATE
elif flower_type == NARCISSUS:
    price = flower_count * NARCIS
    if flower_count < NARCISSUS_COUNT:
        price += price * NARCISSUS_RATE
elif flower_type == GLADIOLUS:
    price = flower_count * GLADIOLA
    if flower_count < GLADIOLUS_COUNT:
        price += price * GLADIOLUS_RATE

if budget >= price:
    remaining = budget - price
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {remaining:.2f} leva left.")
else:
    needed_money = price - budget
    print(f"Not enough money, you need {needed_money:.2f} leva more.")

