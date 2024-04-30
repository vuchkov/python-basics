ROOM_PRICE = 18.00
APP_PRICE = 25.00
VIP_APP_PRICE = 35.00

days = int(input())
room_type = input().strip()
feeling = input().strip()

nights = days - 1

price = 0
if room_type == "room for one person":
    price = ROOM_PRICE
elif room_type == "apartment":
    price = APP_PRICE
elif room_type == "president apartment":
    price = VIP_APP_PRICE

price *= nights
if days < 10:
    if room_type == "apartment":
        price -= price * 30 / 100
    elif room_type == "president apartment":
        price -= price * 10 / 100
elif 10 <= days <= 15:
    if room_type == "apartment":
        price -= price * 35 / 100
    elif room_type == "president apartment":
        price -= price * 15 / 100
elif 15 < days:
    if room_type == "apartment":
        price -= price * 50 / 100
    elif room_type == "president apartment":
        price -= price * 20 / 100

if feeling == "positive":
    price += price * 25 / 100
elif feeling == "negative":
    price -= price * 10 / 100

print(f"{price:.2f}")
