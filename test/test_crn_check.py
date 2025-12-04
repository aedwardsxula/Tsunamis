import unittest
from pathlib import Path
from unittest.mock import patch

from help_desk.crn_check import Course, load_courses, filter_by_subject, select_course


class TestCrnCheck(unittest.TestCase):

    def setUp(self):
        """
        Runs before every test.
        Create a small test CSV file and load it with load_courses().
        This way we are not depending on the real data/data.csv file.
        """
        self.test_csv = Path("test_courses.csv")

        csv_data = """subject,number,title,crn,prerequisites,add_deadline,drop_deadline
CPSC,2735,Data Structures,12345,CPSC 1010,2025-01-20,2025-02-10
MATH,1010,College Algebra,23456,None,2025-01-20,2025-02-10
CPSC,1010,Intro to Programming,34567,None,2025-01-20,2025-02-10
"""

        self.test_csv.write_text(csv_data, encoding="utf-8")
        self.courses = load_courses(self.test_csv)

    def tearDown(self):
        """Remove the temporary CSV file after every test."""
        if self.test_csv.exists():
            self.test_csv.unlink()

    # TEST 1
    def test_load_courses_reads_file(self):
        """load_courses should return Course objects from the CSV."""
        self.assertEqual(len(self.courses), 3)
        self.assertIsInstance(self.courses[0], Course)
        self.assertEqual(self.courses[0].subject, "CPSC")
        self.assertEqual(self.courses[0].crn, "12345")

    # TEST 2
    def test_filter_by_subject_cpsc_only(self):
        """filter_by_subject should return only courses with matching subject."""
        cpsc_courses = filter_by_subject(self.courses, "CPSC")
        self.assertGreater(len(cpsc_courses), 0)
        for course in cpsc_courses:
            self.assertEqual(course.subject, "CPSC")
        subjects = {c.subject for c in cpsc_courses}
        self.assertNotIn("MATH", subjects)

    # TEST 3
    def test_filter_by_subject_case_insensitive(self):
        """Subject filter should be case-insensitive (e.g., 'cPsC')."""
        cpsc_courses = filter_by_subject(self.courses, "cPsC")
        self.assertGreater(len(cpsc_courses), 0)
        for course in cpsc_courses:
            self.assertEqual(course.subject, "CPSC")

    # TEST 4
    @patch("builtins.input", side_effect=["2"])
    def test_select_course_valid_choice(self, mock_input):
        """select_course should return the correct Course for a valid number."""
        cpsc_courses = filter_by_subject(self.courses, "CPSC")
        selected = select_course(cpsc_courses)
        self.assertIsNotNone(selected)
        self.assertEqual(selected, cpsc_courses[1])  # user chose "2"

    # TEST 5
    @patch("builtins.input", side_effect=["10", "1"])
    def test_select_course_reprompts_on_invalid_then_valid(self, mock_input):
        """
        If user enters out-of-range number, select_course should reprompt
        until a valid number is entered.
        """
        cpsc_courses = filter_by_subject(self.courses, "CPSC")
        selected = select_course(cpsc_courses)
        self.assertIsNotNone(selected)
        self.assertEqual(selected, cpsc_courses[0])  # final choice "1"

    # TEST 6
    @patch("builtins.input", side_effect=[""])
    def test_select_course_empty_input_returns_none(self, mock_input):
        """If user just presses Enter, select_course should return None."""
        cpsc_courses = filter_by_subject(self.courses, "CPSC")
        selected = select_course(cpsc_courses)
        self.assertIsNone(selected)


if __name__ == "__main__":
    unittest.main()
