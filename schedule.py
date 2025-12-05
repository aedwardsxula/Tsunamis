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
    crn = str(crn).strip()

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)

        index = {h.strip().lower(): i for i, h in enumerate(headers)}

        for row in reader:
            if not row:
                continue  

            row_crn = row[index["crn"]].strip()
            if row_crn == crn:
                return {
                    "crn": row[index["crn"]].strip(),
                    "subject": row[index["subject"]].strip(),
                    "course_number": row[index["number"]].strip(),
                    "title": row[index["title"]].strip(),
                    "prerequisites": row[index["prerequisites"]].strip(),
                    "add_deadline": row[index["add_deadline"]].strip(),
                    "drop_deadline": row[index["drop_deadline"]].strip(),
                    "days": "",
                    "time": "",
                }

    return None

