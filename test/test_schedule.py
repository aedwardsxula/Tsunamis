import unittest
from schedule import Schedule, load_course_from_csv
from unittest.mock import mock_open, patch


class TestSchedule(unittest.TestCase):

    def test_add_course(self):
        s = Schedule("001", "Austin")
        course = {"crn": "10002", "title": "Math"}

        s.add_course(course)

        self.assertEqual(len(s.courses), 1)
        self.assertEqual(s.courses[0]["crn"], "10002")
    
    def test_is_registered(self):
        s = Schedule("001", "Austin")
        course = {"crn": "10002", "title": "Math"}

        s.add_course(course)

        self.assertTrue(s.is_registered_for("10002"))
    
    def test_is_registered_false(self):
        s = Schedule("001", "Austin")
        course = {"crn": "10002", "title": "Math"}

        s.add_course(course)

        self.assertFalse(s.is_registered_for("100"))
    
    def test_load_course_from_csv_course_found(self):
        sample_csv = (
            "CRN,SUBJ,CRSE,TITLE,DAYS,TIME\n"
            "10001,Math,MATH 1090,Calculus 2, M/W/F, 10:00-10:50\n"
            "20002,Computer Science,CPSC 3140,Data Structures, T/Th, 11:00-11:50\n"
        )
        with patch("builtins.open", mock_open(read_data=sample_csv)):
            course = load_course_from_csv("10001", csv_path="fakeCSV.csv")
        
        self.assertIsNotNone(course)
        self.assertEqual(course["crn"], "10001")
        self.assertEqual(course["subject"], "Math")
        self.assertEqual(course["course_number"], "MATH 1090")

    def test_load_course_from_csv_course_not_found(self):
        sample_csv = (
            "CRN,SUBJ,CRSE,TITLE,DAYS,TIME\n"
            "10001,Math,MATH 1090,Calculus 2, M/W/F, 10:00-10:50\n"
            "20002,Computer Science,CPSC 3140,Data Structures, T/Th, 11:00-11:50\n"
        )
        with patch("builtins.open", mock_open(read_data=sample_csv)):
            course = load_course_from_csv("30003", csv_path="fakeCSV.csv")

        self.assertIsNone(course)

if __name__ == "__main__":
    unittest.main()
