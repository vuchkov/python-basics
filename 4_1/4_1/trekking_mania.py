musala_max = 5
monblan_min = 6
monblan_max = 12
kili_min = 13
kili_max = 25
k2_min = 26
k2_max = 40
everest_min = 41

groups = int(input())
total = 0
group = [0, 0, 0, 0, 0]

for i in range(groups):
    group_members = int(input())
    total += group_members

    if group_members <= musala_max:
        group[0] += group_members
    elif monblan_min <= group_members <= monblan_max:
        group[1] += group_members
    elif kili_min <= group_members <= kili_max:
        group[2] += group_members
    elif k2_min <= group_members <= k2_max:
        group[3] += group_members
    elif everest_min <= group_members:
        group[4] += group_members

for i in range(len(group)):
    percent = group[i] / total * 100
    print(f"{percent:.2f}%")

