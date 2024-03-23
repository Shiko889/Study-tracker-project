from PIL import Image
import sqlite3
import os

class StudyTracker:
    def __init__(self, database_path):
        self.database_path = database_path
        self.create_database()  # Creates the database if it doesn't exist

        # Placeholder for stored studies
        self.stored_studies = {}

        # Placeholder for image
        self.spaced_repetition_image = Image.new("RGB", (100, 100))

        print("Study tracker initialized")  # Print initialization message

    def create_database(self):
        """Creates the SQLite database if it doesn't exist"""
        if not os.path.exists(self.database_path):
            connection = sqlite3.connect(self.database_path)
            cursor = connection.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS studies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    subject TEXT,
                    notes TEXT
                )
            ''')

            connection.commit()
            connection.close()

    def add_new_study(self, name, subject, notes):
        """Adds a new study to the database"""
        connection = sqlite3.connect(self.database_path)
        cursor = connection.cursor()

        cursor.execute("INSERT INTO studies (name, subject, notes) VALUES (?, ?, ?)", (name, subject, notes))

        connection.commit()
        connection.close()

        print("New study added:", name)  # Print confirmation message

    def get_all_studies(self):
        """Fetches all studies from the database"""
        connection = sqlite3.connect(self.database_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM studies")
        studies = cursor.fetchall()

        connection.close()

        return studies

    def show_all(self):
        """Displays all stored studies"""
        studies = self.get_all_studies()
        for study in studies:
            print(study)

    def show_image(self):
        """Placeholder for showing image"""
        print("Showing image")

    def show_review_items(self):
        """Placeholder for showing review items"""
        print("Showing review items")

   
def update_review_item(self, study_name, new_review_date):
    # Logic to update the review item with the given study name and new review date
    print("Updating review item for study:", study_name, "with new review date:", new_review_date)
