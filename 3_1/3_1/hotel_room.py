PRICE_STUDIO_MAY = 50
PRICE_APP_MAY = 65
PRICE_STUDIO_JUNE = 75.20
PRICE_APP_JUNE = 68.70
PRICE_STUDIO_JULY = 76
PRICE_APP_JULY = 77
PRICE_STUDIO_AUG = 76
PRICE_APP_AUG = 77
PRICE_STUDIO_SEP = 75.20
PRICE_APP_SEP = 68.70
PRICE_STUDIO_OCT = 50
PRICE_APP_OCT = 65

DISC_MAY_OCT_7 = 5 / 100
DISC_MAY_OCT_14 = 30 / 100
DISC_JUNE_SEP_14 = 20 / 100
DISC_APP_14 = 10 / 100

month = input().strip()
nights = int(input())

price_studio = 0
price_app = 0
if month == "May" or month == "October":
    price_studio = nights * PRICE_STUDIO_MAY
    price_app = nights * PRICE_APP_MAY
    if nights > 14:
        price_app -= price_app * DISC_APP_14
        price_studio -= price_studio * DISC_MAY_OCT_14
    elif 7 < nights:
        price_studio -= price_studio * DISC_MAY_OCT_7
elif month == "June" or month == "September":
    price_studio = nights * PRICE_STUDIO_JUNE
    price_app = nights * PRICE_APP_JUNE
    if nights > 14:
        price_app -= price_app * DISC_APP_14
        price_studio -= price_studio * DISC_JUNE_SEP_14
elif month == "July" or month == "August":
    price_studio = nights * PRICE_STUDIO_JULY
    price_app = nights * PRICE_APP_JULY
    if nights > 14:
        price_app -= price_app * DISC_APP_14

print(f"Apartment: {price_app:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")
