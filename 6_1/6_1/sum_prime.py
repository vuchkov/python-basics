command = ""
sum_prime = 0
sum_non_prime = 0
while command != "stop":
    command = input()
    if command == "stop":
        break

    number = int(command)
    if number < 0:
        print("Number is negative.")
        continue

    for n in range(2, number + 1):
        if (number % n == 0 and number != n):
            sum_non_prime += number
            break
        if n == number:
            sum_prime += number

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
