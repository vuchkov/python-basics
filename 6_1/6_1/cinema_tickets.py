FINAL = "Finish"
STOP = "End"

STANDARD = "standard"
STUDENT = "student"
KID = "kid"

all_tickets = 0
sum_standard_tickets = 0
sum_student_tickets = 0
sum_kid_tickets = 0

while True:

    movie = input()
    if movie == FINAL:
        break

    seats_in_cinema = int(input())
    seats_taken = 0
    while seats_taken < seats_in_cinema:
        ticket = input()
        if ticket == STOP:
            break

        all_tickets += 1
        seats_taken += 1
        if ticket == STANDARD:
            sum_standard_tickets += 1
        elif ticket == STUDENT:
            sum_student_tickets += 1
        elif ticket == KID:
            sum_kid_tickets += 1

    print(f"{movie} - {seats_taken / seats_in_cinema * 100:.2f}% full.")

print(f"Total tickets: {all_tickets}")
print(f"{sum_student_tickets / all_tickets * 100:.2f}% student tickets.")
print(f"{sum_standard_tickets / all_tickets * 100:.2f}% standard tickets.")
print(f"{sum_kid_tickets / all_tickets * 100:.2f}% kids tickets.")
