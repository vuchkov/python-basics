first_number = int(input())
second_number = int(input())
operator = input().strip()

if second_number == 0 and (operator == "/" or operator == "%"):
    print(f"Cannot divide {first_number} by zero")
    exit()

result = 0
if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    result = first_number / second_number
elif operator == "%":
    result = first_number % second_number

if operator == "+" or operator == "-" or operator == "*":
    even_or_odd = "odd"
    if result % 2 == 0:
        even_or_odd = "even"
    # even_or_odd = "even" if result % 2 == 0 else even_or_odd = "odd"
    print(f"{first_number} {operator} {second_number} = {result} - {even_or_odd}")
elif operator == "/":
    print(f"{first_number} / {second_number} = {result:.2f}")
elif operator == "%":
    print(f"{first_number} % {second_number} = {result}")