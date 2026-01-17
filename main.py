def read_reviews(filename):
    """
    Reads reviews from a text file.

    Args:
        filename (str): path to review file

    Returns:
        list: list of review dictionaries
    """
    reviews = []

    with open(filename) as file:
        for line in file:
            parts = line.strip().split("|")

            title = parts[0].strip()
            rating = int(parts[1].strip())
            text = parts[2].strip()

            reviews.append({
                "title": title,
                "rating": rating,
                "text": text
            })

    return reviews


def find_book_reviews(reviews, book_title):
    """
    Finds all reviews for a given book.

    Args:
        reviews (list): all reviews
        book_title (str): book to search for

    Returns:
        list: reviews for the selected book
    """
    result = []

    for review in reviews:
        if review["title"].lower() == book_title.lower():
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

    for review in reviews:
        if review["rating"] > best_review["rating"]:
            best_review = review

        if review["rating"] < worst_review["rating"]:
            worst_review = review

    print("\nBest review:")
    print(best_review["text"])

    if best_review != worst_review:
        print("\nWorst review:")
        print(worst_review["text"])


filename = "reviews.txt"
all_reviews = read_reviews(filename)

book = input("Enter book title: ")
book_reviews = find_book_reviews(all_reviews, book)

best_and_worst(book_reviews)
