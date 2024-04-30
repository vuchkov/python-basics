PRICE_PREMIERE = 12
PRICE_NORMAL = 7.50
PRICE_DISCOUNT = 5

PROJECTION_PREMIERE = "Premiere"
PROJECTION_NORMAL = "Normal"
PROJECTION_DISCOUNT = "Discount"

projection_type = input().strip()
rows = int(input())
cols = int(input())

total_seats = rows * cols

price = 0
if projection_type == PROJECTION_PREMIERE:
    price = total_seats * PRICE_PREMIERE
elif projection_type == PROJECTION_NORMAL:
    price = total_seats * PRICE_NORMAL
elif projection_type == PROJECTION_DISCOUNT:
    price = total_seats * PRICE_DISCOUNT
else:
    print("Invalid projection type")
    exit()
print(f"{price:.2f} leva")
