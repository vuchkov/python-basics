s = input()
total = 0.0

while s != "NoMoreMoney":
    amount = float(s)
    if amount < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {amount:.2f}")
        total += amount
        s = input()

print(f"Total: {total:.2f}")
