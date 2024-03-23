from studytracker import StudyTracker
from review import Review
from datetime import date

def main():
    # Initialize StudyTracker with the database path
    tracker = StudyTracker("study_database.db")

    while True:
        print("\nStudy Tracker Menu:")
        print("1. Add New Study")
        print("2. Show Review Items")
        print("3. Update Review Item")
        print("4. Show All Studies")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a new study
            study_name = input("Enter study name: ")
            study_subject = input("Enter study subject: ")
            study_notes = input("Enter study notes: ")

            tracker.add_new_study(study_name, study_subject, study_notes)

        elif choice == "2":
            # Show review items
            today = date.today()
            reviews = tracker.get_review_items(today)
            if reviews:
                print("\nStudy topics needing review:")
                for review in reviews:
                    print(review.study)
            else:
                print("No study topics need review at the moment.")

        elif choice == "3":
            # Update review item
            study_name = input("Enter the name of the study to update review date: ")
            new_review_date = input("Enter the new review date (YYYY-MM-DD): ")
            tracker.update_review_date(study_name, new_review_date)

        elif choice == "4":
            # Show all studies
            tracker.show_all()

        elif choice == "5":
            # Exit
            print("Exiting Study Tracker.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

