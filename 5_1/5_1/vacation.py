SPEND = "spend"
SAVE = "save"
MAX_DAYS = 5

needed_money = float(input())
money = float(input())
spend_days_counter = 0
days = 0

while money < needed_money:
    action = input()
    action_amount = float(input())
    days += 1
    if action == SAVE:
        money += action_amount
        spend_days_counter = 0
    elif action == SPEND:
        money -= action_amount
        spend_days_counter += 1
        if spend_days_counter >= MAX_DAYS:
            break
        if money < 0:
            money = 0

if spend_days_counter >= MAX_DAYS:
    print(f"You can't save the money.")
    print(f"{days}")
elif money > 0:
    print(f"You saved the money for {days} days.")
