TEMPERATURE_LOW = 10
TEMPERATURE_MEDIUM = 18
TEMPERATURE_HIGH = 24

OUTFIT_MORNING_LOW_CLOTHES = "Sweatshirt"
OUTFIT_MORNING_LOW_SHOES = "Sneakers"
OUTFIT_MORNING_MEDIUM_CLOTHES = "Shirt"
OUTFIT_MORNING_MEDIUM_SHOES = "Moccasins"
OUTFIT_MORNING_HIGH_CLOTHES = "T-Shirt"
OUTFIT_MORNING_HIGH_SHOES = "Sandals"

OUTFIT_AFTERNOON_LOW_CLOTHES = "Shirt"
OUTFIT_AFTERNOON_LOW_SHOES = "Moccasins"
OUTFIT_AFTERNOON_MEDIUM_CLOTHES = "T-Shirt"
OUTFIT_AFTERNOON_MEDIUM_SHOES = "Sandals"
OUTFIT_AFTERNOON_HIGH_CLOTHES = "Swim Suit"
OUTFIT_AFTERNOON_HIGH_SHOES = "Barefoot"

OUTFIT_EVENING_LOW_CLOTHES = "Shirt"
OUTFIT_EVENING_LOW_SHOES = "Moccasins"
OUTFIT_EVENING_MEDIUM_CLOTHES = "Shirt"
OUTFIT_EVENING_MEDIUM_SHOES = "Moccasins"
OUTFIT_EVENING_HIGH_CLOTHES = "Shirt"
OUTFIT_EVENING_HIGH_SHOES = "Moccasins"

degrees = int(input())
time_of_day = input().strip()

outfit = ""
shows = ""

if 10 <= degrees <= 18:
    if time_of_day == "Morning":
        outfit = OUTFIT_MORNING_LOW_CLOTHES
        shoes = OUTFIT_MORNING_LOW_SHOES
    elif time_of_day == "Afternoon":
        outfit = OUTFIT_AFTERNOON_LOW_CLOTHES
        shoes = OUTFIT_AFTERNOON_LOW_SHOES
    elif time_of_day == "Evening":
        outfit = OUTFIT_EVENING_LOW_CLOTHES
        shoes = OUTFIT_EVENING_LOW_SHOES
elif 18 < degrees <= 24:
    if time_of_day == "Morning":
        outfit = OUTFIT_MORNING_MEDIUM_CLOTHES
        shoes = OUTFIT_MORNING_MEDIUM_SHOES
    elif time_of_day == "Afternoon":
        outfit = OUTFIT_AFTERNOON_MEDIUM_CLOTHES
        shoes = OUTFIT_AFTERNOON_MEDIUM_SHOES
    elif time_of_day == "Evening":
        outfit = OUTFIT_EVENING_MEDIUM_CLOTHES
        shoes = OUTFIT_EVENING_MEDIUM_SHOES
elif 24 <= degrees:
    if time_of_day == "Morning":
        outfit = OUTFIT_MORNING_HIGH_CLOTHES
        shoes = OUTFIT_MORNING_HIGH_SHOES
    elif time_of_day == "Afternoon":
        outfit = OUTFIT_AFTERNOON_HIGH_CLOTHES
        shoes = OUTFIT_AFTERNOON_HIGH_SHOES
    elif time_of_day == "Evening":
        outfit = OUTFIT_EVENING_HIGH_CLOTHES
        shoes = OUTFIT_EVENING_HIGH_SHOES

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")