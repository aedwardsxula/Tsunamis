import csv
from pathlib import Path

class Schedule:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.courses = []

    def add_course(self, course_dict):
        self.courses.append(course_dict)

    def is_registered_for(self, crn):
        for course in self.courses:
            if course.get("crn") == str(crn):
                return True
        return False

COURSE_DATA_PATH = Path("data") / "courses.csv"

def load_course_from_csv(crn, csv_path=COURSE_DATA_PATH):
    crn = str(crn)
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("CRN") == crn:
                return {
                    "crn": row.get("CRN"),
                    "subject": row.get("SUBJ"),
                    "course_number": row.get("CRSE"),
                    "title": row.get("TITLE"),
                    "days": row.get("DAYS"),
                    "time": row.get("TIME"),
                }
    return None
