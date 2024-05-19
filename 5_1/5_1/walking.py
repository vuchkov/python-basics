TARGET = 10000
STOP = "Going home"

steps = 0
while steps <= TARGET:
    command = input()
    if command == STOP:
        steps += int(input())
        break
    else:
        steps += int(command)

if steps >= TARGET:
    print("Goal reached! Good job!")
    steps -= TARGET
    print(f"{steps} steps over the goal!")
else:
    steps = TARGET - steps
    print(f"{steps} more steps to reach goal.")
