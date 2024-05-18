name = input()

total = 0.0
grade = 1
bad_mark_counter = 0
while grade <= 12:
    mark = float(input())
    if mark < 4:
        bad_mark_counter += 1
        if bad_mark_counter > 1:
            break
        continue
    bad_mark_counter = 0
    total += mark
    grade += 1

if bad_mark_counter == 2:
    print(f"{name} has been excluded at {grade} grade")
else:
    mark = total / 12
    print(f"{name} graduated. Average grade: {mark:.2f}")
