facebook = 150
instagram = 100
reddit = 50

open_tabs = int(input())
salary = int(input())
fines = 0

for _ in range(open_tabs):
    site_name = input().lower().strip()

    if site_name == 'facebook':
        fines += facebook
    elif site_name == 'instagram':
        fines += instagram
    elif site_name == 'instagram':
        fines += instagram

if fines >= salary:
    print("You have lost your salary.")
    exit()

print(int(salary - fines))
