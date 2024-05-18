username = input()
password = input()

while True:
    check_password = input()
    if check_password == password:
        print(f"Welcome {username}!")
        break
