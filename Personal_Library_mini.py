# MİNİ Personal Library Application for beginner Pyhton learners ^^

library = []   # List to store books

def add_book():
    book_title = input("Book title: ")
    author = input("Author name: ")
    book = {"book_title": book_title, "author": author}
    library.append(book)
    print(f"'{book_title}' has been successfully added!\n")

def show_books():
    if len(library) == 0:
        print("Library is empty.\n")
    else:
        print("Books in your library:")
        for i, book in enumerate(library, start=1):
            print(f"{i}. {book['book_title']} - {book['author']}")
        print("")

while True:
    print("1. Add book")
    print("2. Show books")
    print("3. Exit")
    choice = input("Your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        show_books()
    elif choice == "3":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice, please try again.\n")
