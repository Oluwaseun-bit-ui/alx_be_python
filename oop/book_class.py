# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor: Called when a new Book instance is created."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Called when the Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation: For print() and user-friendly display."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation: For developers and debugging."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

