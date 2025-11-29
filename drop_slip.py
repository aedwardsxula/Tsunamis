class DropSlip:
    def __init__(self, student_name, student_id, term, course_dict):
        self.student_name = student_name
        self.student_id = student_id
        self.term = term
        self.course = course_dict

    def to_text(self):
        return (
            "===== DROP SLIP =====\n"
            f"Student Name: {self.student_name}\n"
            f"Student ID: {self.student_id}\n"
            f"Term: {self.term}\n\n"
            "Course to Drop:\n"
            f"CRN: {self.course.get('crn', '')}\n"
            f"Course: {self.course.get('subject', '')} {self.course.get('course_number', '')}\n"
            f"Title: {self.course.get('title', '')}\n"
            f"Days: {self.course.get('days', '')}\n"
            f"Time: {self.course.get('time', '')}\n\n"
            "Student Signature: ________________________\n"
            "Date: _______________\n"
        )


def write_drop_slip_to_file(drop_slip, filename="drop_slip.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(drop_slip.to_text())
    return filename
