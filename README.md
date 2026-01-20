# Pre-IB Computer Science Project Documentation

## Project Title

**Book Review Analyzer**

## Target Assessment Level

The target assessment level of this work is **3**.

## Specification

### What does the program do?

This program analyzes book reviews stored in a separate text file, reviews.txt.

Each review contains a book title, a numerical rating, and a short review text.

First, the program reads all reviews from a text file, then asks the user to enter a book title, finds all reivews for that book and finally prints the best review and the worst review.

The program processes text data in a meaningful way but isn't useful in the real world.

### Input

The program uses a text file containing multiple book reviews and user input for selecting the book title.
The user inputs the book title.

### Data Format

The input file (`reviews.txt`) consists of multiple lines.

Each line has the format:

```
book_title | rating | review_text
```

* `book_title` is a single word
* `rating` is an integer from 1 to 5
* `review_text` is free text

Example:

```
Dune | 5 | Deep and well written with amazing world building
```

The program assumes that every line follows this format and it doesn't check for empty lines in the file.

## Correctness

### Typical Test Case

**Input file:** `reviews.txt`

**User input:**

```
Enter book title: Dune
```

**Output:**

```
Best review:
Deep and well written with amazing world building

Worst review:
Too slow and difficult to enjoy
```

The program should find all reviews for the selected book, identify the highest-rated and lowest-rated reviews, and should produce the expected output.

## Resource Management

The program opens the input file using a `with` statement:

```python
with open(filename) as file:
```

This ensures that the file is automatically closed after reading and that no system resources remain open.
