num_count = int(input())

p1_counter = 0
p2_counter = 0
p3_counter = 0
p4_counter = 0
p5_counter = 0

for _ in range(num_count):
    cur_number = int(input())
    if 1 <= cur_number < 200:
        p1_counter += 1
    elif 200 <= cur_number <= 399:
        p2_counter += 1
    elif 400 <= cur_number <= 599:
        p3_counter += 1
    elif 600 <= cur_number <= 799:
        p4_counter += 1
    elif 800 <= cur_number:
        p5_counter += 1

print(f"{p1_counter / num_count * 100:.2f}%")
print(f"{p2_counter / num_count * 100:.2f}%")
print(f"{p3_counter / num_count * 100:.2f}%")
print(f"{p4_counter / num_count * 100:.2f}%")
print(f"{p5_counter / num_count * 100:.2f}%")
