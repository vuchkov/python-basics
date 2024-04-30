exam_hours = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

exam_mins = exam_hours * 60 + exam_min
arrival_mins = arrival_hour * 60 + arrival_min

if arrival_mins < exam_mins - 30:
    print("Early")
elif arrival_mins <= exam_mins:
    print("On time")
else:
    print("Late")

hours = 0
mins = 0
before_after = "after"
if arrival_mins < exam_mins:
    mins = exam_mins - arrival_mins
    before_after = "before"
elif arrival_mins > exam_mins:
    mins = arrival_mins - exam_mins

hours = mins // 60
mins = mins % 60
if hours > 0:
    print(f"{hours}:{mins:02d} hours {before_after} the start")
elif hours == 0 and mins > 0:
    print(f"{mins} minutes {before_after} the start")
