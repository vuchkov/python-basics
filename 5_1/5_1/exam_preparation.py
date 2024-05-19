STOP = "Enough"
BAD_GRADE_THRESHOLD = 4
bad_grades_limit = int(input())

bad_grades_count = 0
problems_count = 0
grade_sum = 0
problem_name = ""

while True:
    command = input()
    if command == STOP:
        break
    problem_name = command
    problems_count += 1
    current_grade = int(input())
    grade_sum += current_grade
    if current_grade <= BAD_GRADE_THRESHOLD:
        bad_grades_count += 1
    if bad_grades_count >= bad_grades_limit:
        break

if bad_grades_count >= bad_grades_limit:
    print(f"You need a break, {bad_grades_count} poor grades.")
else:
    average_grade = grade_sum / problems_count
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {problems_count}")
    print(f"Last problem: {problem_name}")
