x = int(input())
y = int(input())
z = int(input())

current = x * y * z

while current > 0:
    command = input()
    if command == "Done":
        break
    current -= int(command)

if current > 0:
    print(f"{current} Cubic meters left.")
else:
    current = 0 - current
    print(f"No more free space! You need {current} Cubic meters more.")
