class Review:
    def __init__(self, study, review_date):
        """
        Initialize a Review object with study and review_date attributes.

        Args:
            study (str): The name of the study.
            review_date (str): The review date in the format 'YYYY-MM-DD'.
        """
        self.study = study
        self.review_date = review_date

    def __repr__(self):
        """
        Return a string representation of the Review object.
        """
        return f"Review(study='{self.study}', review_date='{self.review_date}')"

    def needs_review(self, current_date):
        """
        Check if the study needs to be reviewed based on its review_date.

        Args:
            current_date (str): The current date in the format 'YYYY-MM-DD'.

        Returns:
            bool: True if the study needs review, False otherwise.
        """
        return current_date >= self.review_date

    def update_review_date(self, new_review_date):
        """
        Update the review date of the study.

        Args:
            new_review_date (str): The new review date in the format 'YYYY-MM-DD'.
        """
        # Additional error handling can be added here to validate the format or date
        self.review_date = new_review_date
