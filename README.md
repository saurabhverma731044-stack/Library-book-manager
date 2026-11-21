# Library Book Manager

A menu-driven command-line application built in Python for managing a library's book inventory, tracking issued and returned copies, and searching records. Developed as **Group 2's Project**, this application demonstrates core Python programming concepts—including dictionaries, tuples, sets, string manipulation, nested loops, and manual input validation—without relying on external libraries or file I/O.

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
