pens = int(input())
markers = int(input())
litres = int(input())
percent = int(input())

total_without_discount = (pens * 5.80) + (markers * 7.20) + (litres * 1.20)
discount = total_without_discount * percent / 100
total = total_without_discount - discount

print(total)
