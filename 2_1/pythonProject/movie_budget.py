DECOR = 10 / 100
CLOTHES = 10 / 100

budget = float(input())
extras = int(input())
clothes_price = float(input())

decor = budget * DECOR
clothes = extras * clothes_price

if extras >= 150:
    clothes -= clothes * CLOTHES

price = decor + clothes

if price <= budget:
    print("Action!")
    remaining = budget - price
    print(f"Wingard starts filming with {remaining:.2f} leva left.")
#     exit(0) and remove else: line.
else:
    print("Not enough money!")
    remaining = price - budget
    print(f"Wingard needs {remaining:.2f} leva more.")
