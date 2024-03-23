import datetime
import unittest
from PIL import Image
from colorama import Fore, Style
from studytracker import StudyTracker


class TestStudyTracker(unittest.TestCase):
    def setUp(self):
        self.study_tracker = StudyTracker()

    def test_init(self):
        self.assertIsInstance(self.study_tracker.stored_studies, dict)
        self.assertIsInstance(self.study_tracker.spaced_repetition_image, Image.Image)

    def test_show_image(self):
        self.assertRaises(NotImplementedError, self.study_tracker.show_image)

    def test_get_input(self):
        self.assertRaises(NotImplementedError, self.study_tracker.get_input)

    def test_add_new_study(self):
        self.assertRaises(NotImplementedError, self.study_tracker.add_new_study)

    def test_show_review_items(self):
        self.assertRaises(NotImplementedError, self.study_tracker.show_review_items)

    def test_update_review_item(self):
        self.assertRaises(NotImplementedError, self.study_tracker.update_review_item)

    def test_show_all(self):
        self.assertRaises(NotImplementedError, self.study_tracker.show_all)


if __name__ == '__main__':
    unittest.main()