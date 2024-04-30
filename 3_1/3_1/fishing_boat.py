SPRING = 3000
SUMMER = 4200
AUTUMN = 4200
WINTER = 2600

DISCOUNT_6 = 10 / 100
DISCOUNT_7_11 = 15 / 100
DISCOUNT_12 = 25 / 100

DISCOUNT_EVEN_WO_AUTUMN = 5 / 100

budget = int(input())
season = input().strip()
fishermen = int(input())

price = 0
if season == "Spring":
    price = SPRING
elif season == "Summer":
    price = SUMMER
elif season == "Autumn":
    price = AUTUMN
elif season == "Winter":
    price = WINTER
else:
    print("Invalid season")
    exit()

if fishermen <= 6:
    price -= price * DISCOUNT_6
elif 7 <= fishermen <= 11:
    price -= price * DISCOUNT_7_11
elif 12 <= fishermen:
    price -= price * DISCOUNT_12

if season != "Autumn" and fishermen % 2 == 0:
    price -= price * DISCOUNT_EVEN_WO_AUTUMN

if budget >= price:
    remaining = budget - price
    print(f"Yes! You have {remaining:.2f} leva left.")
else:
    needed = price - budget
    print(f"Not enough money! You need {needed:.2f} leva.")
