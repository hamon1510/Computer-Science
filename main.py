def read_reviews(filename):
    """
    Reads reviews from a text file.

    Args:
        filename, as a string: path to review file

    Returns:
        list: list of reviews as a list
    """
    reviews = []

    with open(filename) as file:
        for line in file:
            parts = line.strip().split("|")
            title = parts[0].strip()
            rating = int(parts[1].strip())
            text = parts[2].strip()
            reviews.append([title, rating, text]) # this loop splits the book reviews into separate parts and combines it into a list
    return reviews

def find_book_reviews(reviews, book_title):
    """
    Finds all reviews for a given book.

    Args:
        reviews, as a list: all reviews
        book_title, as a string: book to search for

    Returns:
        list: reviews for the selected book
    """
    result = []
    for review in reviews:
        if review[0].lower() == book_title.lower(): # searches index 0, the title of the book in the list
            result.append(review)
    return result

def best_and_worst(reviews):
    """
    Prints the highest-rated and lowest-rated review.

    Args:
        reviews (list): list of reviews for one book
    """
    if len(reviews) == 0:
        print("No reviews found for this book.")
        return

    best_review = reviews[0]
    worst_review = reviews[0]
    
    # this loop checks whether next review is better or worse rated than the previous
    for review in reviews:
        if review[1] > best_review[1]:
            best_review = review

        if review[1] < worst_review[1]:
            worst_review = review
    
    print("\nBest review:")
    print(best_review[2])

    if best_review != worst_review:
        print("\nWorst review:")
        print(worst_review[2])

filename = "reviews.txt"
all_reviews = read_reviews(filename)

book = input("Enter book title: ")
book_reviews = find_book_reviews(all_reviews, book)

best_and_worst(book_reviews)
