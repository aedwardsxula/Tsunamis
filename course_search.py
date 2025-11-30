# course_search.py
# Tsunamis – CPSC Help Desk 
# Implements user story:
# "As a student, I want the app to check whether a course is offered
#  this semester so that I know if I can take it."

class Course:
    """
    Represents a course offering.

    Attributes:
        subject: e.g., "MATH"
        number: e.g., "2550"
        semester: e.g., "Fall 2025"
        crn: course reference number, e.g., "12345"
        instructor: instructor name
        days: meeting days, e.g., "MWF"
        time: meeting time, e.g., "9:00–9:50"
        seats_open: number of open seats
    """

    def __init__(self, subject, number, semester, crn,
                 instructor, days, time, seats_open):
        self.subject = subject
        self.number = number
        self.semester = semester
        self.crn = crn
        self.instructor = instructor
        self.days = days
        self.time = time
        self.seats_open = seats_open

    def course_code(self) -> str:
        """Return a string like 'MATH 2550'."""
        return f"{self.subject} {self.number}"


# -------------------------
# Mock Course Data (TEMP)
# -------------------------

CURRENT_SEMESTER = "Fall 2025"

# In a later sprint, this will come from scraping XULA Course Offerings.
COURSE_OFFERINGS = [
    Course("MATH", "2550", CURRENT_SEMESTER, "12345",
           "Dr. Smith", "MWF", "09:00–09:50", 5),
    Course("CPSC", "2740", CURRENT_SEMESTER, "55678",
           "Dr. Edwards", "TR", "11:00–12:15", 0),  # full example
    Course("BIOL", "1230", CURRENT_SEMESTER, "99887",
           "Dr. King", "MWF", "13:00–13:50", 12),
]


# -------------------------
# Helper Functions
# -------------------------

def normalize_course_code(course_code: str):
    """
    Normalize user input like 'math2550', '  MATH 2550  ' into
    subject='MATH', number='2550'.

    Returns (subject, number) or (None, None) if invalid.
    """
    if course_code is None:
        return None, None

    code = course_code.upper().replace(" ", "")
    subject = "".join(c for c in code if c.isalpha())
    number = "".join(c for c in code if c.isdigit())

    if subject and number:
        return subject, number
    return None, None


def search_course_offerings(course_code: str):
    """
    Search if a course is offered this semester.

    Returns a dict with:
        status: "offered" | "not_found" | "full" | "invalid"
        message: human-readable string
        sections: list[Course] (for 'offered' or 'full')
    """
    subject, number = normalize_course_code(course_code)

    if not subject or not number:
        return {
            "status": "invalid",
            "message": "Invalid course format. Use something like 'MATH 2550'.",
            "sections": [],
        }

    matches = [
        c for c in COURSE_OFFERINGS
        if c.subject == subject
        and c.number == number
        and c.semester == CURRENT_SEMESTER
    ]

    if not matches:
        return {
            "status": "not_found",
            "message": "Course not offered this semester or not found.",
            "sections": [],
        }

    all_full = all(c.seats_open == 0 for c in matches)

    if all_full:
        return {
            "status": "full",
            "message": f"{subject} {number} is offered, but all sections are full.",
            "sections": matches,
        }

    return {
        "status": "offered",
        "message": f"{subject} {number} is offered this semester.",
        "sections": matches,
    }


# -------------------------
# CLI Runner for this story
# -------------------------

def run_course_checker():
    """
    Simple CLI-based flow that matches the user story:

    - Student enters a course code (e.g., MATH 2550)
    - System tells them if it is offered this semester
      and shows sections if available.
    """
    print("\n--- Course Offering Checker ---\n")
    course_code = input("Enter a course code (e.g., MATH 2550): ").strip()

    result = search_course_offerings(course_code)

    print("\n" + result["message"])

    if result["status"] in ("offered", "full"):
        print("\nSections:")
        for c in result["sections"]:
            print(
                f"  CRN: {c.crn} | {c.course_code()} | "
                f"{c.days} {c.time} | Instructor: {c.instructor} | "
                f"Seats open: {c.seats_open}"
            )
    print()


if __name__ == "__main__":
    # Run this file directly to test the user story feature
    run_course_checker()
