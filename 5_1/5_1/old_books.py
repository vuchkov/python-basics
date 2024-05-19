STOP_COMMAND = "No More Books"

favourite_book = input()

book_count = 0
current_book = ""
is_book_found = False

while current_book != STOP_COMMAND and not is_book_found:
    current_book = input()
    if current_book == STOP_COMMAND:
        break
    is_book_found = current_book == favourite_book
    if not is_book_found:
        book_count += 1

if is_book_found:
    print(f"You checked {book_count} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {book_count} books.")
