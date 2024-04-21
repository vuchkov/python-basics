PUZZLE_PRICE = 2.60
DOLL_PRICE = 3.0
BEAR_PRICE = 4.1
MINION_PRICE = 8.2
TRUCK_PRICE = 2.0

DISCOUNT_QTY = 50
DISCOUNT = 25 / 100
RENT = 10 / 100

holiday_price = float(input())
puzzle_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

subtotal = puzzle_count * PUZZLE_PRICE
subtotal += dolls_count * DOLL_PRICE
subtotal += bears_count * BEAR_PRICE
subtotal += minions_count * MINION_PRICE
subtotal += trucks_count * TRUCK_PRICE

count = (puzzle_count + dolls_count
         + bears_count + minions_count
         + trucks_count)

grand_total = subtotal
if count >= DISCOUNT_QTY:
    grand_total = subtotal - subtotal * DISCOUNT

remaining = grand_total - grand_total * RENT

if holiday_price <= remaining:
    money = remaining - holiday_price
    print(f"Yes! {money:0.2f} lv left.")
else:
    money = holiday_price - remaining
    print(f"Not enough money! {money:0.2f} lv needed.")
