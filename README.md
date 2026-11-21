# Library Book Manager

A menu-driven command-line application built in Python for managing a library's book inventory, tracking issued and returned copies, and searching records. Developed as **Group 2's Project**, this application demonstrates core Python programming concepts—including dictionaries, tuples, sets, string manipulation, nested loops, and manual input validation—without relying on external libraries or file.

---

## Table of Contents
- [Team Members](#team-members)
- [Features](#features)
- [Pre-loaded Catalogue](#pre-loaded-catalogue)
- [Getting Started](#getting-started)
- [Usage & Sample Walkthrough](#usage--sample-walkthrough)
- [Data Structures & Architecture](#data-structures--architecture)
- [Function Reference](#function-reference)
- [Input Validation & Edge Cases](#input-validation--edge-cases)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)

---

## Team Members
**Group 2**
- **Saurabh Verma**
- **Dipt Kumar**
- **Prem Bhusawale**
- **Nitin Gupta**

---

## Features

1. **Add Book**
   - Adds a new book with a unique Book ID, title, author, and copy count.
   - Automatically normalizes Book IDs to uppercase and formats titles/authors in Title Case.
   - Prevents duplicate Book IDs from overwriting existing entries.
2. **Issue Book**
   - Checks if the requested Book ID exists and has available copies.
   - Decrements the available count and adds the Book ID to the active `issued_set`.
3. **Return Book**
   - Verifies that the book exists and is currently issued before accepting a return.
   - Increments the available count and removes the ID from `issued_set` once all copies are back in stock.
4. **Search Book**
   - Performs case-insensitive, partial-match searches across both book titles and author names.
5. **Display Full Catalogue**
   - Groups all books alphabetically by author and displays them in a clean, aligned table showing `ID`, `Title`, and `Avail/Total` copies.
6. **Show Total Library Capacity**
   - Calculates and displays the total number of physical book copies across the entire catalogue.

---

## Pre-loaded Catalogue

To make testing immediate, the application initializes with two sample books on startup:

| Book ID | Title | Author | Available | Total Copies |
| :--- | :--- | :--- | :--- | :--- |
| `B001` | Atomic Habits | James Clear | 5 | 5 |
| `B002` | Python Programming | John Zelle | 3 | 3 |

---

## Getting Started

### Prerequisites
- **Python 3.x** (No third-party packages required; uses only standard built-in Python features).

### Installation & Running
1. Clone the repository or download the source file (e.g., `library_manager.py`).
2. Open a terminal or command prompt and navigate to the project directory:
   ```bash
   cd path/to/project
   ```
3. Run the application:
   ```bash
   python library_manager.py
   ```
   *(On some systems, use `python3 library_manager.py`.)*

---

## Usage & Sample Walkthrough

When launched, the program presents an interactive menu:

```text
=== Library Book Manager ===
1. Add Book
2. Issue Book
3. Return Book
4. Search Book
5. Display Full Catalogue
6. Show Total Library Capacity
7. Exit
Enter choice (1-7):
```

### Example: Displaying the Catalogue (Option 5)
```text
-----------------------------------------------------------------
ID       | Title                          | Avail/Total
-----------------------------------------------------------------
Author: James Clear
  B001   | Atomic Habits                  | 5/5
Author: John Zelle
  B002   | Python Programming             | 3/3
-----------------------------------------------------------------
```

### Example: Searching for a Book (Option 4)
```text
Enter title or author to search: python

Search Results:
ID: B002, Title: Python Programming, Author: John Zelle, Available: 3
```

---

## Data Structures & Architecture

The program uses three core Python data structures to manage state efficiently in memory:

1. **`catalogue` (Dictionary):** Maps each unique `b_id` to a nested dictionary containing immutable book metadata and inventory counts.
   ```python
   catalogue = {
       "B001": {
           "details": ("Atomic Habits", "James Clear"),  # Tuple: (title, author)
           "total": 5,
           "available": 5
       }
   }
   ```
2. **`details` (Tuple):** Stores `(title, author)` as an immutable pair since a book's title and author do not change after entry.
3. **`issued_set` (Set):** Stores unique Book IDs that currently have at least one copy checked out, enabling O(1) lookup when validating returns.

---

## Function Reference

| Function | Parameters | Returns | Description |
| :--- | :--- | :--- | :--- |
| `clean_text` | `text` | `str` | Strips leading/trailing whitespace and converts text to Title Case. |
| `add_book` | `catalogue, b_id, title, author, copies` | `bool` | Normalizes inputs and inserts a new book; returns `False` if `b_id` already exists. |
| `issue_book` | `catalogue, issued_set, b_id` | `bool` | Decrements available copies and updates `issued_set`; returns `False` if unavailable or invalid. |
| `return_book` | `catalogue, issued_set, b_id` | `bool` | Increments available copies and cleans up `issued_set` when all copies are returned. |
| `search_books` | `catalogue, query` | `list` | Returns a list of `(b_id, title, author, available)` tuples matching the query. |
| `get_total_copies` | `catalogue` | `int` | Iterates through the catalogue and sums the `total` copies of all books. |
| `display_catalogue` | `catalogue` | `None` | Groups books by author and prints a formatted table using nested loops. |
| `main` | *None* | `None` | Initializes data, runs the CLI menu loop, and handles user input/validation. |

---

## Input Validation & Edge Cases

The application handles invalid user input gracefully using manual checks (without `try-except` blocks):
- **Empty Fields:** Rejects blank Book IDs, titles, authors, or search queries.
- **Invalid Copy Counts:** Ensures the number of copies is a positive integer using `.isdigit()` and `int(copies) > 0`.
- **Duplicate IDs:** Prevents adding a book with an ID that already exists in `catalogue`.
- **Over-Issuing / Over-Returning:** Blocks issuing when `available == 0` and blocks returning when all copies are already in stock or the ID is not in `issued_set`.
- **Case Sensitivity:** Automatically standardizes Book IDs to uppercase and searches in lowercase so user casing doesn't cause mismatches.

---

## Limitations

- **No Persistent Storage:** All changes are stored in memory only. Exiting the program resets the catalogue to the two pre-loaded books.
- **No Borrower Tracking:** The system tracks *which* books are issued, but not *who* borrowed them or when they are due.
- **Single-Session CLI:** Designed for single-user, local terminal use.

---

## Future Enhancements

- **File Persistence:** Save and load the catalogue using JSON or CSV files so data persists across sessions.
- **Member Management:** Track borrower names, member IDs, issue dates, and due dates with overdue fine calculations.
- **Book Removal & Editing:** Add menu options to delete books or update copy counts.
- **Exception Handling:** Introduce `try-except` blocks for more robust error handling when adding file I/O.

