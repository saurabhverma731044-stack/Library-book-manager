'''
Library Book Manager - Group 2 Project
Members: Prem Bhusawale, Dipt Kumar, Nitin Gupta, Saurabh Verma
'''

def clean_text(text):
    '''Cleans input text using string methods.'''
    return text.strip().title()

def add_book(catalogue, b_id, title, author, copies):
    '''
    Adds a new book to the catalogue.
    The fixed details (title, author) are stored as a tuple.
    '''
    b_id = b_id.strip().upper()
    title = clean_text(title)
    author = clean_text(author)

    if b_id in catalogue:
        return False

    # Dictionary storing fixed details as a tuple
    catalogue[b_id] = {
        'details': (title, author),
        'total': copies,
        'available': copies
    }
    return True

def issue_book(catalogue, issued_set, b_id):
    '''Issues a book if available and updates the issued set.'''
    if b_id in catalogue:
        if catalogue[b_id]['available'] > 0:
            catalogue[b_id]['available'] -= 1
            issued_set.add(b_id)  # Using a set for quick lookup/unique records
            return True
    return False

def return_book(catalogue, issued_set, b_id):
    '''Returns an issued book and updates the issued set.'''
    if b_id in catalogue and b_id in issued_set:
        if catalogue[b_id]['available'] < catalogue[b_id]['total']:
            catalogue[b_id]['available'] += 1
            # Remove from issued_set only when all copies are returned
            if catalogue[b_id]['available'] == catalogue[b_id]['total']:
                issued_set.remove(b_id)
            return True
    return False

def search_books(catalogue, query):
    '''Searches for a book by title or author.'''
    query = query.strip().lower()
    results = []
    for b_id, data in catalogue.items():
        title, author = data['details']
        if query in title.lower() or query in author.lower():
            results.append((b_id, title, author, data['available']))
    return results

def get_total_copies(catalogue):
    '''Counts total copies held by the library using a simple loop.'''
    total = 0
    for data in catalogue.values():
        total += data['total']
    return total

def display_catalogue(catalogue):
    '''Displays the catalogue using nested loops, grouped by author.'''
    authors = {}
    for b_id, data in catalogue.items():
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

def main():
    '''Main menu driven loop without exception handling or file I/O.'''
    catalogue = {}
    issued_set = set()

    # Pre-loaded books so the catalogue is not empty at startup
    add_book(catalogue, "B001", "Atomic Habits", "James Clear", 5)
    add_book(catalogue, "B002", "Python Programming", "John Zelle", 3)

    while True:
        print("\n=== Library Book Manager ===")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Search Book")
        print("5. Display Full Catalogue")
        print("6. Show Total Library Capacity")
        print("7. Exit")

        choice = input("Enter choice (1-7): ").strip()

        if choice == '1':
            b_id = input("Enter Book ID (e.g., B003): ").strip()
            title = input("Enter Title: ").strip()
            author = input("Enter Author: ").strip()
            copies = input("Enter Number of Copies: ").strip()

            if not b_id or not title or not author:
                print("Error: Book ID, Title, and Author cannot be empty.")
                continue

            # Simple manual check instead of try-except
            if not copies.isdigit() or int(copies) <= 0:
                print("Error: Copies must be a positive integer.")
                continue

            if add_book(catalogue, b_id, title, author, int(copies)):
                print("Book added successfully.")
            else:
                print("Error: A book with this ID already exists.")

        elif choice == '2':
            b_id = input("Enter Book ID to issue: ").strip().upper()
            if issue_book(catalogue, issued_set, b_id):
                print("Book issued successfully.")
            else:
                print("Error: Book not available or invalid ID.")

        elif choice == '3':
            b_id = input("Enter Book ID to return: ").strip().upper()
            if return_book(catalogue, issued_set, b_id):
                print("Book returned successfully.")
            else:
                print("Error: Book not issued or invalid ID.")

        elif choice == '4':
            query = input("Enter title or author to search: ").strip()
            if not query:
                print("Error: Search query cannot be empty.")
                continue

            results = search_books(catalogue, query)
            if results:
                print("\nSearch Results:")
                for b_id, title, author, avail in results:
                    print(f"ID: {b_id}, Title: {title}, Author: {author}, Available: {avail}")
            else:
                print("No books found matching your query.")

        elif choice == '5':
            if not catalogue:
                print("Catalogue is empty.")
            else:
                display_catalogue(catalogue)

        elif choice == '6':
            total = get_total_copies(catalogue)
            print(f"Total copies of all books in library: {total}")

        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == '__main__':
    main()