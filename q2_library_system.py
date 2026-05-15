def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)
    print("Book added:", title)


def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print("Book borrowed:", catalog[book_id][0])
    else:
        print("Book cannot be borrowed")


def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print("Book returned:", book_id)
    else:
        print("Book was not borrowed")


def register_member(members, member_id):
    members.add(member_id)


def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")

    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            print(book_id, "->", details)


def main():
    catalog = {}
    borrowed_books = []
    members = set()

    # Adding books
    add_book(catalog, 101, "Python Basics", "John", 2020)
    add_book(catalog, 102, "Data Structures", "Smith", 2019)
    add_book(catalog, 103, "AI Fundamentals", "David", 2021)
    add_book(catalog, 104, "Machine Learning", "Andrew", 2022)

    # Registering members
    register_member(members, 1)
    register_member(members, 2)
    register_member(members, 3)
    register_member(members, 2)

    print("\nMembers:", members)

    # Borrow books
    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)

    print("\nBorrowed Books:", borrowed_books)

    # Return one book
    return_book(borrowed_books, 101)

    print("\nBorrowed Books After Return:", borrowed_books)

    # Show available books
    show_available(catalog, borrowed_books)


main()
