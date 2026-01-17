# Pre-IB Computer Science Project Documentation

## Project Title

**Book Review Analyzer**

## Target Assessment Level

Target assessment level of this work is **3**.

## Specification

### What does the program do?

The program analyzes book reviews stored in a text file.

Each review contains a book title, a numerical rating, and a short review text.

The program:

1. Reads all reviews from a text file
2. Asks the user to enter a book title
3. Finds all reviews for that book
4. Prints the **best review** (highest rating) and the **worst review** (lowest rating)

The program processes text data in a meaningful way but does not attempt to be a real-world application.

### Input

The program uses a text file containing multiple book reviews and user input for selecting the book title.
The user inputs the book title using the keyboard.

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
HarryPotter | 5 | The book was detailed and interesting
```

The program assumes that every line follows this format and that there are no empty lines in the file.

## Correctness

### Typical Test Case

**Input file:** `reviews.txt`

**User input:**

```
Enter book title: HarryPotter
```

**Output:**

```
Best review:
The book was detailed and interesting

Worst review:
Poor pacing and uninteresting plot
```

The program correctly finds all reviews for the selected book, identifies the highest-rated and lowest-rated reviews, and produces the expected output.

## Resource Management

The program opens the input file using a `with` statement:

```python
with open(filename) as file:
```

This ensures that the file is automatically closed after reading and that no system resources remain open.