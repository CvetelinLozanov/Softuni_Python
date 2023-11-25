searching_book = input()
number_of_books = 0

while True:
    book = input()

    if book == 'No More Books':
        print(f'The book you search is not here!\nYou checked {number_of_books} books.')
        break

    if book == searching_book:
        print(f'You checked {number_of_books} books and found it.')
        break

    number_of_books += 1
