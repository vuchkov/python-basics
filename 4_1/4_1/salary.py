facebook = 150
instagram = 100
reddit = 50

open_tabs = int(input())
salary = int(input())
fines = 0

for _ in range(open_tabs):
    site_name = input()

    if site_name == 'Facebook':
        fines += facebook
    elif site_name == 'Instagram':
        fines += instagram
    elif site_name == 'Reddit':
        fines += instagram

if fines >= salary:
    print("You have lost your salary.")
    exit()

print(int(salary - fines))
