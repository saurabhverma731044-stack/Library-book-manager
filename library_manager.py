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