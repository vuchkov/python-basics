DISCOUNT_100_SUMMER = 30 / 100
DISCOUNT_100_WINTER = 70 / 100
DISCOUNT_1000_SUMMER = 40 / 100
DISCOUNT_1000_WINTER = 80 / 100

HIGH_BUDGET_EUROPE = 90 / 100

DESTINATION_LOW = "Bulgaria"
DESTINATION_MID = "Balkans"
DESTINATION_HIGH = "Europe"

CAMP = "Camp"
HOTEL = "Hotel"

budget = float(input())
season = input().strip()

price = budget
destination = ""
accommodation = ""
if 0 < budget <= 100:
    destination = DESTINATION_LOW
    if season == "summer":
        price = price * DISCOUNT_100_SUMMER
        accommodation = CAMP
    else:
        price = price * DISCOUNT_100_WINTER
        accommodation = HOTEL
elif 100 < budget <= 1000:
    destination = DESTINATION_MID
    if season == "summer":
        price = price * DISCOUNT_1000_SUMMER
        accommodation = CAMP
    else:
        price = price * DISCOUNT_1000_WINTER
        accommodation = HOTEL
elif 1000 < budget:
    destination = DESTINATION_HIGH
    price = price * HIGH_BUDGET_EUROPE
    accommodation = HOTEL

if budget >= price:
    print(f"Somewhere in {destination}")
    print(f"{accommodation} - {price:.2f}")
