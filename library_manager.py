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


# Calculating available copies 

book_id = "B101"

# total = books[book_id][2]
# issued = issue_records.count(book_id)
# available = total - issued

# print("Book:", books[book_id][0])
# print("Total Copies:", total)
# print("Issued Copies:", issued)
# print("Available Copies:", available)

#showing the issued books

# print("Currently issued books :", issued_book_ids)

def calculate_available(book_id):
    total=books[book_id][2]
    issued=issue_records.count(book_id)
    available=total-issued
    return available

results=calculate_available("A101")
print("Available copies : " ,results)

def calculate_issued(book_id):
    issued=issue_records.count(book_id)
    return issued



# FEATURE 1: ADD A NEW BOOK
# This function allows the librarian to add a new book
# to the library by entering its ID, title, author and copies.

def add_book():

    print("\n----- ADD NEW BOOK -----")

    # Taking the unique Book ID from the user.
    book_id = input("Enter Book ID: ").strip().upper()

    # Checking whether this Book ID already exists.
    # Every book must have a unique ID.
    if book_id in books:
        print("This Book ID already exists!")
        return

    # Taking the remaining book details.
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()

    # Converting the number of copies into an integer.
    try:
        copies = int(input("Enter Number of Copies: "))

        # A book must have at least one copy.
        if copies <= 0:
            print("Number of copies must be greater than zero!")
            return

    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    # Checking that title and author are not empty.
    if title == "" or author == "":
        print("Book title and author cannot be empty!")
        return

    # Adding the new book to the dictionary.
    # Book ID becomes the key.
    # Book details are stored together as a tuple.
    books[book_id] = (title, author, copies)

    print("\nBook added successfully!")
    print("Book ID:", book_id)
    print("Book Title:", title)
    print("Author:", author)
    print("Total Copies:", copies)

    return True

