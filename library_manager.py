#Books_detail
# we are storing books records with the book id,
#  giving them book name with author name and number of copies
#  available there.

books={
    "A101":("Atomic Habits","James Clear",5),
    "A102":("October Junction","Divyapraksash Dubey",5),
    "B101":("Python Programming","Ajay Sonkar",10),
    "B102":("Linear Algebra","Abhinav Mishra",9)
}

#storing records of issued book, like if we want to know how many books have been issued,
#we can just enter book id and find out. for this i will use list, because it allows
#duplication.

issue_records=["A101","B101","A101"]

issued_book_ids=set(issue_records)





def calculate_available(book_id):
    """
    Calculate the number of available copies of a book.

    >>> calculate_available("A101")
    3
    >>> calculate_available("B101")
    9
    """

    total = books[book_id][2]
    issued = issue_records.count(book_id)
    available = total - issued

    return available



def calculate_issued(book_id):
    """
    Calculate how many copies of a book are issued.

    >>> calculate_issued("A101")
    2
    >>> calculate_issued("B101")
    1
    """

    issued = issue_records.count(book_id)

    return issued


# HELPER FUNCTION 1: VALIDATE BOOK ID
# Checks whether the given Book ID exists in the library.

def is_valid_book_id(book_id):

    if book_id in books:
        return True

    return False




# FEATURE 1: ADD A NEW BOOK
# This function allows the librarian to add a new book
# to the library by entering its ID, title, author and copies.


# FEATURE 10A: ADD A NEW BOOK WITH INPUT VALIDATION

def add_book():

    print("\n----- ADD NEW BOOK -----")

    # Taking the unique Book ID from the user.
    book_id = input("Enter Book ID: ").strip().upper()

    # Check whether Book ID is empty.
    if book_id == "":
        print("Book ID cannot be empty!")
        return False

    # Check whether Book ID already exists.
    if book_id in books:
        print("This Book ID already exists!")
        return False

    # Taking book title and author name.
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()

    # Check whether title or author is empty.
    if title == "" or author == "":
        print("Book title and author cannot be empty!")
        return False

    # Prevent the file separator from appearing in book details.
    if "|" in book_id or "|" in title or "|" in author:
        print("Book ID, title and author cannot contain '|'.")
        return False

    # Taking number of copies.
    try:
        copies = int(input("Enter Number of Copies: "))

        # Copies must be positive.
        if copies <= 0:
            print("Number of copies must be greater than zero!")
            return False

    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return False

    # Add the new book to the dictionary.
    books[book_id] = (title, author, copies)

    print("\nBook added successfully!")
    print("Book ID:", book_id)
    print("Book Title:", title)
    print("Author:", author)
    print("Total Copies:", copies)

    return True




# FEATURE 2: ISSUE A BOOK
# This function allows the librarian to issue a book.
# It checks availability before issuing the book.

def issue_book():

    print("\n----- ISSUE A BOOK -----")

    # Taking the Book ID from the user.
    book_id = input("Enter Book ID to issue: ").strip().upper()

    # Check whether Book ID is empty.
    if book_id == "":
        print("Book ID cannot be empty!")
        return False

    # Step 1: Check whether the Book ID exists.
    if not is_valid_book_id(book_id):
        print("Book ID does not exist!")
        return False

    

    # Step 2: Calculate how many copies are available.
    available = calculate_available(book_id)

    # Step 3: Stop if no copies are available.
    if available <= 0:
        print("Sorry! No copies are currently available.")
        return False

    # Step 4: Add the issued book ID to the list.
    # A list allows duplicate IDs because multiple copies
    # of the same book can be issued.
    issue_records.append(book_id)

    # Step 5: Add the ID to the set.
    # A set stores each issued Book ID only once.
    issued_book_ids.add(book_id)

    print("\nBook issued successfully!")
    print("Book Title:", books[book_id][0])
    print("Issued Copies:", calculate_issued(book_id))
    print("Available Copies:", calculate_available(book_id))

    return True




# FEATURE 3: RETURN A BOOK
# This function allows the librarian to accept a returned book.

def return_book():

    print("\n----- RETURN A BOOK -----")

    # Taking the Book ID from the user.
    book_id = input("Enter Book ID to return: ").strip().upper()
    # Check whether Book ID is empty.
    if book_id == "":
        print("Book ID cannot be empty!")
        return False

    # Step 1: Check whether the Book ID exists.
    if not is_valid_book_id(book_id):
        print("Book ID does not exist!")
        return False

    # Step 2: Check whether any copy of this book is issued.
    if book_id not in issue_records:
        print("No issued copy of this book was found!")
        return False

    # Step 3: Remove only ONE occurrence from the list.
    # If A101 appears twice, one return leaves one A101.
    issue_records.remove(book_id)

    # Step 4: Update the set.
    # Remove the ID only when no copies remain issued.
    if book_id not in issue_records:
        issued_book_ids.remove(book_id)

    print("\nBook returned successfully!")
    print("Book Title:", books[book_id][0])
    print("Remaining Issued Copies:", calculate_issued(book_id))
    print("Available Copies:", calculate_available(book_id))

    return True


    
# FEATURE 4: SEARCH BOOKS
# This function searches books using their title or author name.
# It also supports partial searches.

def search_book():

    print("\n----- SEARCH BOOKS -----")

    # Taking the search keyword from the user.
    keyword = input("Enter Book Title or Author Name: ").strip().lower()

    # Checking whether the user entered something.
    if keyword == "":
        print("Search keyword cannot be empty!")
        return []

    # This list will store all matching books.
    results = []

    # Traversing through the complete books dictionary.
    for book_id, details in books.items():

        # Extracting title and author from the tuple.
        title = details[0]
        author = details[1]

        # Checking whether keyword exists in title or author.
        if keyword in title.lower() or keyword in author.lower():

            # Storing matching book details.
            results.append((book_id, details))

    # Displaying the search results.
    if len(results) == 0:
        print("No matching books found!")

    else:
        print("\nMatching Books:")
        print("-" * 65)
        print(f"{'Book ID':<12}{'Title':<25}{'Author':<20}{'Copies':<8}")
        print("-" * 65)

        for book_id, details in results:
            print(f"{book_id:<12}{details[0]:<25}{details[1]:<20}{details[2]:<8}")

        print("-" * 65)

    return results




# FEATURE 5: DISPLAY COMPLETE LIBRARY CATALOGUE
# This function displays all books grouped by their authors.
# It uses nested loops to display books author-wise.

def display_catalogue():

    print("\n========== LIBRARY CATALOGUE ==========")

    # Step 1: Get all unique author names.
    # A set automatically removes duplicate author names.
    authors = set()

    for details in books.values():
        authors.add(details[1])

    # Step 2: Sort author names alphabetically.
    sorted_authors = sorted(authors)

    # Step 3: Check whether the library is empty.
    if len(books) == 0:
        print("No books available in the library!")
        return

    # Step 4: Outer loop selects one author at a time.
    for author in sorted_authors:

        print("\nAuthor:", author)
        print("-" * 75)

        # Displaying table headings.
        print(f"{'Book ID':<12}{'Book Title':<30}{'Total':<10}{'Issued':<10}{'Available':<10}")
        print("-" * 75)

        # Inner loop checks every book for the selected author.
        for book_id, details in books.items():

            title = details[0]
            book_author = details[1]
            total = details[2]

            # Display only books belonging to the selected author.
            if book_author == author:

                issued = calculate_issued(book_id)
                available = calculate_available(book_id)

                print(f"{book_id:<12}{title:<30}{total:<10}{issued:<10}{available:<10}")

        print("-" * 75)

    return True




# FEATURE 6: CALCULATE TOTAL COPIES USING RECURSION
# This function calculates the total number of physical copies
# available in the library using recursion.


def calculate_total_copies(book_ids=None):
    """
    Calculate total library copies using recursion.

    >>> calculate_total_copies()
    29
    >>> calculate_total_copies([])
    0
    """

    if book_ids is None:
        book_ids = list(books.keys())

    if len(book_ids) == 0:
        return 0

    book_id = book_ids[0]
    copies = books[book_id][2]

    remaining_copies = calculate_total_copies(book_ids[1:])

    return copies + remaining_copies




# FEATURE 7A: SAVE LIBRARY DATA
# This function saves books and issue records
# permanently into library_data.txt.

def save_data():

    try:
        # Open the text file in write mode.
        # "w" creates the file if it does not exist.
        # If it exists, old content is replaced.
        with open("library_data.txt", "w", encoding="utf-8") as file:

            # First section: Save all book details.
            file.write("BOOKS\n")

            for book_id, details in books.items():

                title = details[0]
                author = details[1]
                copies = details[2]

                # Store each book in one line.
                file.write(f"{book_id}|{title}|{author}|{copies}\n")

            # Second section: Save issued book records.
            file.write("ISSUED\n")

            for book_id in issue_records:
                file.write(book_id + "\n")

        print("Library data saved successfully!")
        return True

    except OSError:
        print("Error! Unable to save library data.")
        return False



# FEATURE 7B: LOAD LIBRARY DATA
# This function reads saved information from library_data.txt
# and restores the original data structures.

def load_data():

    # Temporary containers to store the loaded information.
    loaded_books = {}
    loaded_issue_records = []

    try:
        # Open the file in read mode.
        with open("library_data.txt", "r", encoding="utf-8") as file:

            section = ""

            books_section_found = False
            issued_section_found = False

            # Read the file one line at a time.
            for line in file:

                line = line.strip()

                # Skip empty lines.
                if line == "":
                    continue

                # Identify the BOOKS section.
                if line == "BOOKS":
                    if books_section_found:
                        raise ValueError("Duplicate BOOKS section.")

                    section = "books"
                    books_section_found = True
                    continue

                # Identify the ISSUED section.
                if line == "ISSUED":
                    if issued_section_found:
                        raise ValueError("Duplicate ISSUED section.")

                    section = "issued"
                    issued_section_found = True
                    continue

                # Load book details.
                if section == "books":

                    details = line.split("|")

                    if len(details) != 4:
                        raise ValueError("Invalid book record in file.")

                    book_id = details[0]
                    title = details[1]
                    author = details[2]
                    copies = int(details[3])

                    # Validate Book ID, title, author and copies.
                    if (book_id == "" or title == "" or author == ""
                            or book_id in loaded_books or copies <= 0):

                        raise ValueError("Invalid book information in file.")

                    loaded_books[book_id] = (title, author, copies)

                # Load issued book IDs.
                elif section == "issued":

                    if line not in loaded_books:
                        raise ValueError("Invalid issued Book ID in file.")

                    loaded_issue_records.append(line)

                else:
                    raise ValueError("Invalid file format.")

        # Both sections must exist in the data file.
        if not books_section_found or not issued_section_found:
            raise ValueError("Required sections are missing.")

        # Check that issued copies do not exceed total copies.
        for book_id in loaded_books:
            if loaded_issue_records.count(book_id) > loaded_books[book_id][2]:
                raise ValueError("Issued copies exceed total copies.")

        # Replace existing data with the loaded data.
        books.clear()
        books.update(loaded_books)

        issue_records.clear()
        issue_records.extend(loaded_issue_records)

        # Rebuild the set from the updated issue records.
        issued_book_ids.clear()
        issued_book_ids.update(issue_records)

        print("Library data loaded successfully!")
        return True

    except FileNotFoundError:
        print("Data file not found! Starting with default books.")
        return False

    except (ValueError, OSError):
        print("Error! Library data file is invalid or cannot be read.")
        return False







# FEATURE 8: MAIN MENU
# This function connects all library features.
# It allows the librarian to operate the system through a menu.


def main():

    # Load previously saved data when the program starts.
    load_data()

    # Keep displaying the menu until the user exits.
    while True:


        print("\n========== LIBRARY BOOK MANAGER ==========")
        print("1. Add a Book")
        print("2. Issue a Book")
        print("3. Return a Book")
        print("4. Search Books")
        print("5. Display Complete Catalogue")
        print("6. Calculate Total Library Copies")
        print("7. Save Library Data")
        print("8. Exit")
        print("==========================================")

        # Taking the user's choice.
        choice = input("Enter your choice (1-8): ").strip()

        # Execute the selected feature.
        if choice == "1":
            add_book()

        elif choice == "2":
            issue_book()

        elif choice == "3":
            return_book()

        elif choice == "4":
            search_book()

        elif choice == "5":
            display_catalogue()

        elif choice == "6":
            total = calculate_total_copies()
            print("Total Copies in Library:", total)

        elif choice == "7":
            save_data()

        elif choice == "8":
            # Save all changes before exiting.
            save_data()
            print("Thank you for using Library Book Manager!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 8.")


# Start the program.
if __name__ == "__main__":
    main()




