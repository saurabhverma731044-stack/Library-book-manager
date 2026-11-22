# Library Book Manager

A menu-driven command-line application built in Python for managing a library's book inventory, adding stock to existing titles, tracking issued and returned copies, and searching records. Developed as **Group 2's Project**, this application demonstrates core Python programming concepts—dictionaries, tuples, sets, string methods, nested loops, and manual input validation—without relying on external libraries, exception handling (`try-except`), recursion, or file I/O.

## Team Members

**Group 2**

- **Prem Bhusawale** (`@bhusawaleprem1-debug`)
- **Dipt Kumar** (`@Diptkumar`)
- **Nitin Gupta** (`@ni3guptaa`)
- **Saurabh Verma** (`@saurabhverma731044-stack`)

## Features

1. **Add Book / Add Copies**
   - Adds a new book to `lab_data` with a unique Book ID, title, author, and copy count.
   - Automatically normalizes Book IDs to uppercase and formats titles and authors in Title Case.
   - Supports restocking existing titles: entering an existing Book ID displays the current title and author and adds the new copies to both `total` and `available` counts.
2. **Issue Book**
   - Checks whether the requested Book ID exists in `lab_data` and has at least one available copy.
   - Decrements the `available` count by 1 and records the Book ID in `issued_set`.
3. **Return Book**
   - Verifies that the book exists in `lab_data`, is present in `issued_set`, and has fewer available copies than total copies.
   - Increments the `available` count by 1 and removes the ID from `issued_set` once all copies are back in stock.
4. **Search Book**
   - Performs case-insensitive, partial-match searches across both book titles and author names.
5. **Display Full library Data**
   - Groups all books alphabetically by author and prints an aligned table showing `ID`, `Title`, and `Avail/Total` copies using nested loops.
6. **Show Total Library Capacity**
   - Iterates through `lab_data` and displays the total number of physical book copies held by the library.

## Pre-loaded Library Data

To ensure `lab_data` is not empty at startup, two books are pre-loaded when the program launches:

| Book ID | Title | Author | Available | Total Copies |
| :--- | :--- | :--- | :---: | :---: |
| `B001` | Atomic Habits | James Clear | 5 | 5 |
| `B002` | Python Programming | John Zelle | 3 | 3 |

## Getting Started

### Prerequisites

- **Python 3.x** (Uses only built-in Python features; no external packages required.)

### Installation & Running

1. Clone the repository:
   ```bash
   git clone https://github.com/saurabhverma731044-stack/Library-book-manager.git
   ```
2. Navigate into the project directory:
   ```bash
   cd Library-book-manager
   ```
3. Run the application:
   ```bash
   python library_manager.py
   ```
   *(On macOS/Linux, you may need to run `python3 library_manager.py`.)*

## Usage & Sample Walkthrough

Launching the script opens an interactive menu:

```text
=== Library Book Manager ===
1. Add Book / Add Copies
2. Issue Book
3. Return Book
4. Search Book
5. Display Full library Data
6. Show Total Library Capacity
7. Exit
Enter choice (1-7):
```

### Example: Adding Copies to an Existing Book (Option 1)

```text
Enter Book ID (e.g., B003): b001
Book already exists: 'Atomic Habits' by James Clear.
Enter Number of Copies to Add: 2
Additional copies added successfully.
```

### Example: Searching for a Book (Option 4)

```text
Enter title or author to search: python

Search Results:
ID: B002, Title: Python Programming, Author: John Zelle, Available: 3
```

### Example: Displaying the Full Library Data (Option 5)

```text
-----------------------------------------------------------------
ID       | Title                          | Avail/Total
-----------------------------------------------------------------
Author: James Clear
  B001   | Atomic Habits                  | 7/7
Author: John Zelle
  B002   | Python Programming             | 3/3
-----------------------------------------------------------------
```

## Data Structures & Architecture

The program manages library state in memory using three core Python data structures:

1. **`lab_data` (`dict`)**: Maps each normalized uppercase `b_id` to a nested dictionary storing immutable book details and stock counts.
   ```python
   lab_data = {
       "B001": {
           "details": ("Atomic Habits", "James Clear"),  # Tuple: (title, author)
           "total": 5,
           "available": 5
       }
   }
   ```
2. **`details` (`tuple`)**: Stores `(title, author)` as an immutable pair since a book's core metadata stays fixed once added.
3. **`issued_set` (`set`)**: Tracks unique Book IDs that currently have at least one copy checked out, providing fast membership checks during returns.

## Function Reference

| Function | Parameters | Returns | Description |
| :--- | :--- | :--- | :--- |
| `clean_text` | `text` | `str` | Strips surrounding whitespace and converts text to Title Case. |
| `add_book` | `lab_data, b_id, title, author, copies` | `str` | Normalizes inputs; adds copies to an existing book and returns `"updated"`, or creates a new entry and returns `"added"`. |
| `issue_book` | `lab_data, issued_set, b_id` | `bool` | Decrements `available` by 1 and adds `b_id` to `issued_set`; returns `False` if unavailable or invalid. |
| `return_book` | `lab_data, issued_set, b_id` | `bool` | Increments `available` by 1 and removes `b_id` from `issued_set` when all copies are returned; returns `False` if not issued or invalid. |
| `search_books` | `lab_data, query` | `list` | Performs a case-insensitive title/author search and returns matching `(b_id, title, author, available)` tuples. |
| `get_total_copies` | `lab_data` | `int` | Loops over `lab_data.values()` and returns the total copy count across all books. |
| `display_lab_data` | `lab_data` | `None` | Groups books alphabetically by author and prints a formatted 65-character-wide table using nested loops. |
| `main` | *None* | `None` | Pre-loads starter books into `lab_data`, runs the menu loop, and validates all CLI inputs manually. |

## Input Validation & Edge Cases

All user inputs are validated manually without `try-except` blocks:

- **Empty Fields**: Rejects blank Book IDs, titles, authors, and search queries.
- **Invalid Copy Counts**: Uses `.isdigit()` and `int(copies) > 0` to ensure copy counts are positive integers.
- **Existing Book IDs**: Entering an existing Book ID in Option 1 switches to add-copies mode, preserving the original title and author while increasing `total` and `available` stock.
- **Over-Issuing & Over-Returning**: Blocks issuing when `available == 0` and blocks returning when `b_id` is not in `issued_set` or `available == total`.
- **Case Normalization**: Standardizes Book IDs to uppercase, titles/authors to Title Case, and search queries to lowercase so casing differences do not cause mismatches.

## Limitations

- **In-Memory Storage Only**: `library_manager.py` does not perform file I/O; exiting the program resets `lab_data` to the two pre-loaded books.
- **No Borrower Tracking**: Tracks which Book IDs have copies checked out, but not borrower names or due dates.
- **Single-Session CLI**: Designed for local, single-user terminal execution.

## Future Enhancements

- **Persistent Storage**: Save and load library data using JSON, CSV, or text files so inventory changes persist across sessions.
- **Member & Due-Date Tracking**: Record borrower details, issue dates, due dates, and overdue fines.
- **Book Removal & Editing**: Add menu options to remove titles, reduce copy counts, or edit metadata.
- **Exception Handling**: Introduce `try-except` blocks when integrating file I/O or external data sources.