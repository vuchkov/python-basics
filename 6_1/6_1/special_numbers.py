LEFT = 1111
RIGHT = 9999

number = int(input())

for current_number in range(LEFT, RIGHT + 1):
    is_special = True
    s = str(current_number)
    for _, value in enumerate(s):
        if value == "0":
            is_special = False
            break

        if number % int(value) != 0:
            is_special = False
            break

    if is_special:
        print(current_number, end=" ")
