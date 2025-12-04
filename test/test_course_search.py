import unittest
from help_desk.course_search import (
    Course,
    CURRENT_SEMESTER,
    COURSE_OFFERINGS,
    search_course_offerings, 
)


class TestCourseSearch(unittest.TestCase):
    """Unit tests for 'check whether a course is offered this semester'."""

    def test_offered_course_returns_offered_status(self):
        """A course that exists this semester should return status 'offered'."""
        result = search_course_offerings("MATH 2550")
        self.assertEqual(result["status"], "offered")
        self.assertGreater(len(result["sections"]), 0)
        self.assertIn("offered this semester", result["message"])

    def test_course_not_offered_returns_not_found_status(self):
        """A course that does not exist should return status 'not_found'."""
        result = search_course_offerings("MATH 9999")
        self.assertEqual(result["status"], "not_found")
        self.assertIn("not offered", result["message"].lower())

    def test_all_sections_full_returns_full_status(self):
        """
        If the course is offered but all sections are full,
        status should be 'full'.
        Assumes CPSC 2740 in COURSE_OFFERINGS has seats_open == 0.
        """
        full_sections = [
            c for c in COURSE_OFFERINGS
            if c.subject == "CPSC"
            and c.number == "2740"
            and c.semester == CURRENT_SEMESTER
            and c.seats_open == 0
        ]
        self.assertGreater(
            len(full_sections),
            0,
            "Test data must include at least one full CPSC 2740 section",
        )

        result = search_course_offerings("CPSC 2740")
        self.assertEqual(result["status"], "full")
        self.assertGreater(len(result["sections"]), 0)
        self.assertIn("full", result["message"].lower())

    def test_invalid_course_format_returns_invalid_status(self):
        """Bad or empty input should return status 'invalid'."""
        result = search_course_offerings("2550")  # no subject
        self.assertEqual(result["status"], "invalid")
        self.assertIn("invalid", result["message"].lower())

        result2 = search_course_offerings("")  # empty
        self.assertEqual(result2["status"], "invalid")
        self.assertIn("invalid", result2["message"].lower())

    def test_case_insensitive_and_whitespace_input(self):
        """Input like 'math2550' or '  MATH 2550 ' should still work."""
        result = search_course_offerings("math2550")
        self.assertEqual(result["status"], "offered")

        result2 = search_course_offerings("   MATH   2550   ")
        self.assertEqual(result2["status"], "offered")


if __name__ == "__main__":
    unittest.main()
