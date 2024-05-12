BDAY_MONEY_INC = 10
LITTLE_BROTHER_TAX = 1

age = int(input())
washing_machine_price = float(input())
toy_sell_price = int(input())

money_for_bday = 0
money_saved = 0
toys_count = 0
money_from_toys = 0

for bday in range(1, age + 1):
    if bday % 2 == 0:
        money_for_bday += 10
        money_saved += money_for_bday
        money_saved -= LITTLE_BROTHER_TAX
    else:
        toys_count += 1

money_from_toys = toys_count * toy_sell_price
total_money_saved = money_saved + money_from_toys

diff = abs(total_money_saved - washing_machine_price)

if total_money_saved >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
