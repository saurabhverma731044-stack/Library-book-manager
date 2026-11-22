# Library Book Manager

A menu-driven command-line Python application for managing a library's book inventory, issuing and returning copies, searching records, tracking total stock capacity, and persisting data between sessions in a plain-text file.

Built as **Group 2's Python Project** using only the Python 3 standard library—no external dependencies required.

Repository: [saurabhverma731044-stack/Library-book-manager](https://github.com/saurabhverma731044-stack/Library-book-manager)

## Team Members (Group 2)

| Name | GitHub Handle |
| :--- | :--- |
| Prem Bhusawale | `@bhusawaleprem1-debug` |
| Dipt Kumar | `@Diptkumar` |
| Nitin Gupta | `@ni3guptaa` |
| Saurabh Verma | `@saurabhverma731044-stack` |

## Features

* **Add Book / Add Copies**: Register new books with a unique Book ID, title, author, and copy count, or add extra copies to an existing Book ID. Book IDs are normalized to uppercase and titles/authors to Title Case.
* **Issue Book**: Lend out a single copy of a book if the ID exists and at least one copy is available, decrementing the available count and recording the ID in `issued_set`.
* **Return Book**: Process a returned copy for an issued book without exceeding total stock, removing the ID from `issued_set` once all copies are back on the shelf.
* **Search Book**: Perform case-insensitive partial-match searches across both book titles and author names.
* **Display Full Library Data**: Group all books alphabetically by author using nested loops and display an aligned summary table (`ID`, `Title`, `Avail/Total`).
* **Show Total Library Capacity**: Compute and display the total number of book copies owned by the library across all records.
* **Persistent File Storage**: Automatically load saved books and issued records from `library_data.txt` at startup and save the latest state back to `library_data.txt` on exit.

## Project Structure

| File | Description |
| :--- | :--- |
| [`library_manager.py`](https://github.com/saurabhverma731044-stack/Library-book-manager/blob/main/library_manager.py) | Main CLI application containing core inventory functions, file persistence, and the interactive menu loop. |
| [`library_data.txt`](https://github.com/saurabhverma731044-stack/Library-book-manager/blob/main/library_data.txt) | Plain-text data store for saved book records (`BOOKS`) and currently issued Book IDs (`ISSUED`). |
| [`README.md`](https://github.com/saurabhverma731044-stack/Library-book-manager/blob/main/README.md) | Project documentation, usage guide, and function reference. |

## Getting Started

### Prerequisites

* Python 3.x installed on your system (no third-party packages needed).

### Installation and Running

```bash
git clone https://github.com/saurabhverma731044-stack/Library-book-manager.git
cd Library-book-manager
python3 library_manager.py
```

On Windows, you may run `python library_manager.py` instead of `python3 library_manager.py`.

## Interactive Menu

The program presents seven menu options:

| Option | Action |
| :---: | :--- |
| `1` | **Add Book / Add Copies** — Create a new entry or increase stock for an existing Book ID. |
| `2` | **Issue Book** — Issue one available copy by Book ID. |
| `3` | **Return Book** — Return one issued copy by Book ID. |
| `4` | **Search Book** — Search books by title or author keyword. |
| `5` | **Display Full library Data** — Print all books grouped alphabetically by author. |
| `6` | **Show Total Library Capacity** — Display the sum of total copies across all books. |
| `7` | **Exit** — Save current library data to `library_data.txt` and exit. |

## Data Structures and Storage Format

### In-Memory Structures

* **`lab_data` (`dict`)**: Maps each uppercase Book ID to a dictionary containing an immutable `(title, author)` tuple and integer copy counts:
  ```python
  {
      "B001": {
          "details": ("Atomic Habits", "James Clear"),
          "total": 5,
          "available": 5
      }
  }
  ```
* **`issued_set` (`set`)**: Stores unique Book IDs that currently have at least one copy checked out for fast membership checks.

### File Format (`library_data.txt`)

Records are saved in UTF-8 plain text with two sections—`BOOKS` (pipe-delimited `ID|Title|Author|Total|Available`) and `ISSUED` (one sorted Book ID per line):

```text
BOOKS
B001|Atomic Habits|James Clear|5|5
B002|Python Programming|John Zelle|3|3
T001|Python Basics|Ajay Sonkar|4|4
ISSUED
```

If `library_data.txt` is missing or unreadable on startup, `main()` initializes `lab_data` with two fallback entries:

| Book ID | Title | Author | Total Copies | Available |
| :--- | :--- | :--- | :---: | :---: |
| `B001` | Atomic Habits | James Clear | 5 | 5 |
| `B002` | Python Programming | John Zelle | 3 | 3 |

## Function Reference

| Function | Parameters | Description |
| :--- | :--- | :--- |
| `clean_text` | `text` | Strips surrounding whitespace and converts text to Title Case. |
| `add_book` | `lab_data, b_id, title, author, copies` | Adds a new book (`"added"`) or adds copies to an existing Book ID (`"updated"`). |
| `issue_book` | `lab_data, issued_set, b_id` | Issues one copy if available, updates `issued_set`, and returns `True` or `False`. |
| `return_book` | `lab_data, issued_set, b_id` | Returns one issued copy, removes the ID from `issued_set` when all copies are back, and returns `True` or `False`. |
| `search_books` | `lab_data, query` | Returns a list of `(b_id, title, author, available)` tuples matching `query` in title or author. |
| `get_total_copies` | `lab_data` | Sums and returns the total number of copies across all books in `lab_data`. |
| `display_lab_data` | `lab_data` | Groups books by author and prints a formatted table sorted alphabetically by author. |
| `save_data` | `lab_data, issued_set` | Writes `lab_data` and `issued_set` to `library_data.txt`; handles `OSError`. |
| `load_data` | `lab_data, issued_set` | Reads `library_data.txt` into `lab_data` and `issued_set`; handles `FileNotFoundError`, `ValueError`, and `OSError`. |
| `main` | *(none)* | Initializes state, loads saved or default books, and runs the interactive menu loop. |

## Core Python Concepts Demonstrated

* **Data Structures**: Nested dictionaries, immutable tuples for fixed book metadata, and sets for unique issued-book tracking.
* **String Processing**: `.strip()`, `.upper()`, `.lower()`, `.title()`, `.split("|")`, and f-string column alignment.
* **Control Flow**: Menu-driven `while True` loop, nested `for` loops for author-grouped display, and manual positive-integer validation with `.isdigit()`.
* **File I/O and Exception Handling**: Reading and writing UTF-8 text files via `with open(...)` and catching `FileNotFoundError`, `ValueError`, and `OSError`.