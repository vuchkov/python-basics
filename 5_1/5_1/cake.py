length = int(input())
width = int(input())

pieces = length * width

while pieces > 0:
    command = input()
    if command == "STOP":
        break
    pieces -= int(command)

if pieces > 0:
    print(f"{pieces} pieces are left.")
else:
    pieces = 0 - pieces
    print(f"No more cake left! You need {pieces} pieces more.")
