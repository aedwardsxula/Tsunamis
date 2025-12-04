from dataclasses import dataclass
from typing import List
import csv
from pathlib import Path
import re 


DATA_FILE = Path("data") / "courses.csv"


@dataclass
class Course:
    subject: str
    number: str
    title: str
    crn: str
    prerequisites: str
    add_deadline: str
    drop_deadline: str


def load_courses(csv_path: Path = DATA_FILE) -> List[Course]:
    if not csv_path.exists():
        raise FileNotFoundError(f"Course data file not found: {csv_path}")

    courses: List[Course] = []
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            courses.append(
                Course(
                    subject=row["subject"].strip().upper(),
                    number=row["number"].strip(),
                    title=row["title"].strip(),
                    crn=row["crn"].strip(),
                    prerequisites=row["prerequisites"].strip(),
                    add_deadline=row["add_deadline"].strip(),
                    drop_deadline=row["drop_deadline"].strip(),
                )
            )
    return courses


def filter_by_subject(courses: List[Course], subject: str) -> List[Course]:
    subject = subject.strip().upper()
    return [c for c in courses if c.subject == subject]


COURSE_CODE_PATTERN = re.compile(r"^[A-Z]{2,4}\s+\d{3,4}$")

def validate_course_code(raw_code: str) -> str:
    """
    Validate and normalize a course code like 'MATH 2550'.
    Returns the cleaned code ('MATH 2550') or raises ValueError with a  error message.
    """
    if raw_code is None or raw_code.strip() == "":
        raise ValueError("Course code is required.")

    cleaned = " ".join(raw_code.upper().split())

    if not COURSE_CODE_PATTERN.match(cleaned):
        raise ValueError("Course code must look like 'SUBJ 1234', e.g. 'MATH 2550'.")

    return cleaned


def find_sections_for_code(courses: List[Course], course_code: str) -> List[Course]:
    """
    Find all Course rows whose subject+number match the given code.
    Example course_code: 'MATH 2550'
    """
    subject, number = course_code.split()

    return [
        c for c in courses
        if c.subject == subject and c.number == number
    ]

def check_course_availability(course_code_input: str, courses: List[Course]) -> str:
    """
    Returns a message describing whether the course is offered this semester,
    and lists matching sections (CRN and title).
    """
    try:
        code = validate_course_code(course_code_input)
    except ValueError as exc:
        return f"Error: {exc}"

    matches = find_sections_for_code(courses, code)

    if not matches:
        return f"{code} is not offered this semester."

    lines = [f"{code} is offered this semester. Matching sections:"]
    for c in matches:
        lines.append(f"CRN {c.crn} | {c.title}")

    return "\n".join(lines)


def prompt_subject() -> str:
    return input("Enter a subject code (e.g., MATH, CPSC, ENGL): ").strip()


def show_course_list(courses_for_subject: List[Course]) -> None:
    print("\nAvailable courses:")
    for idx, course in enumerate(courses_for_subject, start=1):
        print(f"{idx}. {course.subject} {course.number} - {course.title}")


def select_course(courses_for_subject: List[Course]) -> Course | None:
    if not courses_for_subject:
        return None

    while True:
        choice = input(
            "\nEnter the number of the course you want to view "
            "(or press Enter to cancel): "
        ).strip()

        if choice == "":
            return None

        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        index = int(choice)
        if 1 <= index <= len(courses_for_subject):
            return courses_for_subject[index - 1]
        else:
            print("That number is not in the list. Try again.")


def show_course_details(course: Course) -> None:
    print("\n=== Course Details ===")
    print(f"Course: {course.subject} {course.number} - {course.title}")
    print(f"CRN: {course.crn}")
    print(f"Prerequisites: {course.prerequisites or 'None'}")
    print(f"Add deadline: {course.add_deadline}")
    print(f"Drop deadline: {course.drop_deadline}")
    print("======================\n")


def run_crn_lookup() -> None:
    all_courses = load_courses()

    subject = prompt_subject()
    courses_for_subject = filter_by_subject(all_courses, subject)

    if not courses_for_subject:
        print(f"No courses found for subject '{subject}'.")
        return

    show_course_list(courses_for_subject)
    selected = select_course(courses_for_subject)

    if selected is None:
        print("No course selected.")
        return

    show_course_details(selected)


if __name__ == "__main__":
    # Testing 
    run_crn_lookup()
