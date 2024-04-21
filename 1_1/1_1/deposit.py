deposit = float(input())
period = int(input())
percentage = float(input()) / 100

money = deposit + period * ((deposit * percentage) / 12)
print(money)