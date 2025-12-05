from crn_check import run_crn_lookup
from schedule import Schedule, load_course_from_csv
from drop_slip import DropSlip, write_drop_slip_to_file
from resources import (
    load_default_resources,
    get_drop_deadline_info,
    load_professor_contacts,
)
from PerformScraping import Scraper


class Driver:
    def main(self):
        while True:
            print("\nWelcome to the Tsunamis CPSC Help Desk!\n")
            print("1) Find the drop date for your semester")
            print("2) Look up a course CRN, prerequisites, and add/drop dates")
            print("3) Create a drop slip for a course")
            print("4) Calculate my GPA")
            print("5) Check if a course is offered this semester")
            print("0) Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.show_drop_dates()
            elif choice == "2":
                run_crn_lookup()
            elif choice == "3":
                self.create_drop_slip()
            elif choice == "4":
                print("GPA calculator not implemented.")
            elif choice == "5":
                self.run_course_offering_check()
            elif choice == "0":
                print("\nGoodbye from the Tsunamis CPSC Help Desk!\n")
                break
            else:
                print("\nInvalid choice. Please try again.\n")

    def show_drop_dates(self):
        semester_drop_dates = Scraper.getDropDates(None)

        print("\nFind the drop date for your semester!")
        usrchoice = input(
            "Which semester are you looking for? (Fall/Spring/Summer): "
        ).strip().lower()
        print()

        found = False
        for key, values in semester_drop_dates.items():
            if usrchoice in key.lower():
                found = True
                for value in values:
                    print("Drop Dates:", value)

        if not found:
            print("Sorry, no drop dates found for that semester.")

    def create_drop_slip(self):
        student_name = input("Enter your full name: ").strip()
        student_id = input("Enter your student ID: ").strip()
        term = input("Enter the term (e.g., Fall 2025): ").strip()
        crn = input("Enter the CRN you want to drop: ").strip()

        course = load_course_from_csv(crn)
        if course is None:
            print("No course found with that CRN.")
            return

        schedule = Schedule(student_id, student_name)
        schedule.add_course(course)

        slip = DropSlip(student_name, student_id, term, course)
        filename = write_drop_slip_to_file(slip)
        print("Drop slip created:", filename)

    def run_course_offering_check(self):
        print("Course offering check not implemented in this snippet.")


if __name__ == "__main__":
    driver = Driver()
    driver.main()
