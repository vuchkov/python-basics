s = float(input())
if s <= 10:
    print("slow")
elif s <= 50:
    print("average")
elif s <= 150:
    print("fast")
elif s <= 1000:
    print("ultra fast")
else:
    print("extremely fast")