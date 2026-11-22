'''Library Book Manager - Group 2 Project
Members: Prem Bhusawale, Dipt Kumar, Nitin Gupta, Saurabh Verma'''

def clean_text(text):
    # Cleans input text using string methods
    return text.strip().title()

def add_book(lab_data, b_id, title, author, copies):
    '''
    Adds a new book to the lab_data, or adds more copies if the Book ID already exists.
    The fixed details (title, author) are stored as a tuple.
    '''
    b_id = b_id.strip().upper()
    title = clean_text(title)
    author = clean_text(author)

    if b_id in lab_data:
        lab_data[b_id]['total'] += copies
        lab_data[b_id]['available'] += copies
        return "updated"

    # Dictionary storing fixed details as a tuple
    lab_data[b_id] = {
        'details': (title, author),
        'total': copies,
        'available': copies
    }
    return "added"
# This function adds a new book or increases the stock of an existing one.
#If b_id is already in the
# lab_data, both total and available counts are increased by copies and the
# function returns "updated". Otherwise, it creates a new dictionary entry
# storing (title, author) as an immutable tuple alongside total and available
# copy counts, then returns "added".

def issue_book(lab_data, issued_set, b_id):
    '''Issues a book if available and updates the issued set.'''
    if b_id in lab_data:
        if lab_data[b_id]['available'] > 0:
            lab_data[b_id]['available'] -= 1
            issued_set.add(b_id)  # Using a set for quick lookup/unique records
            return True
    return False
# This function handles lending out a single copy of a book. It checks that
# b_id exists in the lab_data and that at least one copy is currently
# available. When both conditions pass, it reduces available by 1, records b_id
# in issued_set (a set avoids duplicate IDs and gives fast membership checks),
# and returns True; otherwise it returns False.

def return_book(lab_data, issued_set, b_id):
    # Returns an issued book and updates the issued set
    if b_id in lab_data and b_id in issued_set:
        if lab_data[b_id]['available'] < lab_data[b_id]['total']:
            lab_data[b_id]['available'] += 1
            # Remove from issued_set only when all copies are returned
            if lab_data[b_id]['available'] == lab_data[b_id]['total']:
                issued_set.remove(b_id)
            return True
    return False
# This function processes a book return. It verifies that b_id is in both the
# lab_data and issued_set, and checks available < total so returned copies
# never exceed total stock. After incrementing available by 1, it removes b_id
# from issued_set only when all copies are back on the shelf, then returns
# True; if the book was not issued or the ID is invalid, it returns False.


def search_books(lab_data, query):
    # Searches for a book by title or author
    query = query.strip().lower()
    results = []
    for b_id, data in lab_data.items():
        title, author = data['details']
        if query in title.lower() or query in author.lower():
            results.append((b_id, title, author, data['available']))
    return results
# This function finds books matching a title or author keyword. Converting
# query, title, and author to lowercase makes the search case-insensitive.
# The loop unpacks the stored (title, author) tuple for each entry and appends
# a tuple of (b_id, title, author, available) to results whenever the query
# appears in either field.


def get_total_copies(lab_data):
    # Counts total copies held by the library using a simple loop
    total = 0
    for data in lab_data.values():
        total += data['total']
    return total
# This function calculates the total number of book copies owned by the
# library. It initializes total to 0 and iterates over lab_data.values(),
# adding each book's total copy count in a simple loop before returning the
# final sum.


def display_lab_data(lab_data):
    # Displays the lab_data using nested loops, grouped by author
    authors = {}
    for b_id, data in lab_data.items():
        author = data['details'][1]
        if author not in authors:
            authors[author] = []
        authors[author].append((b_id, data['details'][0], data['available'], data['total']))

    print("-" * 65)
    print(f"{'ID':<8} | {'Title':<30} | {'Avail/Total'}")
    print("-" * 65)

    # Nested loops: Outer loop iterates through authors, inner through their books
    for author in sorted(authors.keys()):
        print(f"Author: {author}")
        for b_id, title, avail, total in authors[author]:
            print(f"  {b_id:<6} | {title:<30} | {avail}/{total}")
    print("-" * 65)
# This function prints the full lab_data grouped alphabetically by author.
# The first loop builds a temporary authors dictionary mapping each author
# name to a list of their books. Next, f-string width specifiers (:<8, :<30)
# and dashed lines print a clean table header. Finally, nested loops iterate
# through sorted(authors.keys()) in the outer loop and each author's book
# list in the inner loop to display aligned ID, title, and avail/total columns.


def save_data(catalogue, issued_set):

    try:

        with open("library_data.txt", "w", encoding="utf-8") as file:

            file.write("BOOKS\n")

            for b_id, data in catalogue.items():

                title, author = data['details']
                total = data['total']
                available = data['available']

                record = f"{b_id}|{title}|{author}|{total}|{available}\n"

                file.write(record)

            file.write("ISSUED\n")

            for b_id in sorted(issued_set):
                file.write(b_id + "\n")

        print("Library data saved successfully!")
        return True

    except OSError:
        print("Error: Unable to save library data.")
        return False


    
def load_data(catalogue, issued_set):

    loaded_catalogue = {}
    loaded_issued = set()

    section = ""

    try:
        with open("library_data.txt", "r", encoding="utf-8") as file:

            for line in file:

                line = line.strip()

                if line == "":
                    continue

                if line == "BOOKS":
                    section = "books"
                    continue

                if line == "ISSUED":
                    section = "issued"
                    continue

                if section == "books":

                    parts = line.split("|")

                    if len(parts) != 5:
                        raise ValueError

                    b_id = parts[0]
                    title = parts[1]
                    author = parts[2]
                    total = int(parts[3])
                    available = int(parts[4])

                    loaded_catalogue[b_id] = {
                        'details': (title, author),
                        'total': total,
                        'available': available
                    }

                elif section == "issued":
                    loaded_issued.add(line)

        catalogue.clear()
        catalogue.update(loaded_catalogue)

        issued_set.clear()
        issued_set.update(loaded_issued)

        print("Library data loaded successfully!")
        return True

    except FileNotFoundError:
        print("No saved data found.")
        return False

    except (ValueError, OSError):
        print("Error: Unable to load valid library data.")
        return False


def main():
    # Main menu driven loop without exception handling or file I/O
    lab_data = {}
    issued_set = set()


    loaded = load_data(lab_data, issued_set)

    if not loaded:

    

    # Pre-loaded books so the lab_data is not empty at startup
        add_book(lab_data, "B001", "Atomic Habits", "James Clear", 5)
        add_book(lab_data, "B002", "Python Programming", "John Zelle", 3)


    while True:
        print("\n=== Library Book Manager ===")
        print("1. Add Book / Add Copies")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Search Book")
        print("5. Display Full library Data")
        print("6. Show Total Library Capacity")
        print("7. Exit")

        choice = input("Enter choice (1-7): ").strip()
 # This while True loop keeps the menu active until the user chooses to
        # exit. Printing the numbered options and calling strip() on choice
        # prevents leading or trailing spaces from causing an invalid choice.

        if choice == '1':
            b_id = input("Enter Book ID (e.g., B003): ").strip().upper()
            if not b_id:
                print("Error: Book ID cannot be empty.")
                continue

            if b_id in lab_data:
                title, author = lab_data[b_id]['details']
                print(f"Book already exists: '{title}' by {author}.")
                copies = input("Enter Number of Copies to Add: ").strip()

                # Simple manual check instead of try-except
                if not copies.isdigit() or int(copies) <= 0:
                    print("Error: Copies must be a positive integer.")
                    continue

                add_book(lab_data, b_id, title, author, int(copies))
                print("Additional copies added successfully.")
            else:
                title = input("Enter Title: ").strip()
                author = input("Enter Author: ").strip()
                copies = input("Enter Number of Copies: ").strip()

                if not title or not author:
                    print("Error: Title and Author cannot be empty.")
                    continue

                # Simple manual check instead of try-except
                if not copies.isdigit() or int(copies) <= 0:
                    print("Error: Copies must be a positive integer.")
                    continue

                add_book(lab_data, b_id, title, author, int(copies))
                print("Book added successfully.")

        elif choice == '2':
            b_id = input("Enter Book ID to issue: ").strip().upper()
            if issue_book(lab_data, issued_set, b_id):
                print("Book issued successfully.")
            else:
                print("Error: Book not available or invalid ID.")

        elif choice == '3':
            b_id = input("Enter Book ID to return: ").strip().upper()
            if return_book(lab_data, issued_set, b_id):
                print("Book returned successfully.")
            else:
                print("Error: Book not issued or invalid ID.")

        elif choice == '4':
            query = input("Enter title or author to search: ").strip()
            if not query:
                print("Error: Search query cannot be empty.")
                continue

            results = search_books(lab_data, query)
            if results:
                print("\nSearch Results:")
                for b_id, title, author, avail in results:
                    print(f"ID: {b_id}, Title: {title}, Author: {author}, Available: {avail}")
            else:
                print("No books found matching your query.")

        elif choice == '5':
            if not lab_data:
                print("Library data is empty.")
            else:
                display_lab_data(lab_data)

        elif choice == '6':
            total = get_total_copies(lab_data)
            print(f"Total copies of all books in library: {total}")

        elif choice == '7':
            save_data(lab_data, issued_set)
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == '__main__':
    main()
# This standard Python guard ensures main() runs automatically only when the
# script is executed directly, preventing it from running if the file is
# imported elsewhere.