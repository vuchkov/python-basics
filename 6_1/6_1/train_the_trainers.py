judges = int(input())

command = ""
count = 0
mark = 0.0
total_mark = 0.0
total_count = 0
while command != "Finish":
    command = input()
    if command == "Finish":
        break

    presentation = command
    total_count += 1
    for count in range(1, judges + 1):
        mark += float(input())
    mark = mark / count
    print(f"{presentation} - {mark:.2f}.")
    total_mark += mark
    mark = 0.0
    count = 0
total_mark = total_mark / total_count
print(f"Student's final assessment is {total_mark:.2f}.")
