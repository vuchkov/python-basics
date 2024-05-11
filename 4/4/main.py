# n = int(input())
# for i in range(1, n, 1):
#     print(i, end="% ")

# n = int(input())
# for i in range(0, n + 1, 2):
#     print(2 ** i)

# n = int(input())
# for i in range(n, 0, -1):
#         print(i)

# text = input()
# for char in text:
#     print(char)

text = input()
points = 0
for char in text:
    match char:
        case 'a':
            points += 1
        case 'e':
            points += 2
        case 'i':
            points += 3
        case 'o':
            points += 4
        case 'u':
            points += 5
print(points)


