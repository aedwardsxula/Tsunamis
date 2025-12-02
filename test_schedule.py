import unittest
from schedule import Schedule, load_course_from_csv

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
