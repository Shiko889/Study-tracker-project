class Customer:
    def __init__(self, name):
        self.name = name
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def __repr__(self):
        return f"Customer(name='{self.name}', reviews={self.reviews})"
