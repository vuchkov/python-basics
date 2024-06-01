command = ""
while command != "End":

    money = 0

    command = input()
    if command == "End":
        break

    destination = command
    required = int(input())

    while money == 0 or money < required:
        command = input()
        if command == "End":
            break
        money += int(command)
    print(f"Going to {destination}!")