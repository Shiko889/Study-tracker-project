class Study:
    def __init__(self, name, initial_review_date):
        self.name = name
        self.initial_review_date = initial_review_date
        self.review_count = 0

    def increment_review_count(self):
        self.review_count += 1

    def update_initial_review_date(self, new_date):
        self.initial_review_date = new_date

    def __repr__(self):
        return f"Study(name='{self.name}', initial_review_date='{self.initial_review_date}', review_count={self.review_count})"
