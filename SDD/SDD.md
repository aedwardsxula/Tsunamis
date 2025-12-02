# **Software Design Document (SDD)**
## **CPSC Help Desk – MVP Release #1**
### Team Tsunamis – Fall 2025

---

# **1. Introduction**
The CPSC Help Desk is a command-line application designed for Xavier University students.
It helps students quickly access academic information such as:

* GPA calculation 
* Course offering availability
* CRN lookup and course info
* Drop deadlines
* Drop slip creation
* Professor contacts and academic resources  
---

# **2. System Overview**
The Help Desk currently supports these major features:
1. Drop Deadline Checker – scrapes XULA academic dates S
2. CRN Lookup – finds course info based on CRN
3. Drop Slip Generator – outputs formatted drop slip file
4. GPA Calculator – calculates weighted GPA
5. Course Offering Checker – checks if a course is offered
6. Professor Resources Loader – advising links & contacts
7. Integrated driver.py menu – all features in one entry point
8. Automated test suite – full coverage using unittest
---

# **3. System Architecture**

                               +----------------------+
                               |      driver.py       |
                               |  (Main Application)  |
                               +----------+-----------+
                                          |
       -------------------------------------------------------------------------
      |                |                |               |                |     
      v                v                v               v                v     
+------------+   +-------------+   +-------------+  +-------------+  +-------------+
|  Scraper   |   | CRN Lookup  |   | Drop Slip   |  |   GPA Calc  |  | Course      |
| (Perform-  |   | (crn_check) |   | (drop_slip) |  | (gpa_calc)  |  | Offering    |
| Scraping)  |   +-------------+   +-------------+  +-------------+  | (course_    |
+------+-----+                                              ^        |  search)    |
       |                                                    |        +------+-------+
       |                                                    |               |
       v                                                    |               |
+------------------+                                        |               |
| Drop Deadline    |                                        |               |
|  Extraction      |                                        |               |
+------------------+                                        |               |
                                                             |               v
                                                             |        +-------------+
                                                             |        |  Resources  |
                                                             |        | (professor  |
                                                             |        |  contacts & |
                                                             |        |   links)    |
                                                             |        +-------------+
                                                             |
                                                             |
       -------------------------------------------------------------------------
       |                               |                                      |
       v                               v                                      v
+----------------------+   +-------------------------+       +--------------------------+
| test_gpa_calculator  |   | test_course_search.py  |       | test_crn_check.py        |
| (Unit Tests)         |   | (Tests course offering)|       | (Tests CRN lookup)        |
+----------------------+   +-------------------------+       +--------------------------+
       |                               |                                      |
       v                               v                                      v
+----------------------+   +-------------------------+       +--------------------------+
| test_dropslip.py     |   | test_schedule.py       |       | test_resources.py         |
| (Drop slip tests)    |   | (Schedule/CSV tests)   |       | (Professor links tests)   |
+----------------------+   +-------------------------+       +--------------------------+


---
# 4. User Stories (MVP)

## 4.1 User Story: Drop Deadline Checker
**As a student, I want the app to tell me the last day to drop a course so that I don’t miss deadlines.**

### Acceptance Criteria
- Student can select a semester (Fall/Spring/Summer).
- System displays correct drop deadline from scraped academic calendar.
- System handles invalid or misspelled semester input.
- If calendar data cannot load, system shows a clear error message.

---

## 4.2 User Story: GPA Calculator
**As a student, I want the app to calculate my GPA so that I understand my academic standing.**

### Acceptance Criteria
- Student can enter multiple courses with grades and credit hours.
- GPA is calculated using the proper grade → quality points conversion.
- GPA is rounded to two decimals.
- System rejects invalid grades and missing credit hours.
- Errors are shown clearly (e.g., “Invalid grade entered”).

---

## 4.3 User Story: Course Offering Checker
**As a student, I want to check whether a course is offered this semester so that I know if I can take it.**

### Acceptance Criteria
- Student enters a course code (e.g., MATH 2550).
- System validates subject + number format.
- System returns one of:
  - **offered** + list of sections  
  - **full** + list of full sections  
  - **not offered**  
  - **invalid course format**
- System is case-insensitive and whitespace-tolerant.

---

## 4.4 User Story: CRN Lookup
**As a student, I want the app to look up a course’s CRN, prerequisites, and add/drop dates so that I can plan my schedule.**

### Acceptance Criteria
- Student can search by CRN or course number.
- System displays:
  - CRN  
  - prerequisites  
  - title  
  - instructor  
  - meeting time & days  
  - add/drop deadlines  
- If course does not exist → “No course found with that CRN.”

---

## 4.5 User Story: Drop Slip Generator
**As a student, I want the app to generate a drop slip for my course so that I can submit it to the registrar.**

### Acceptance Criteria
- Student enters name, XULA ID, term, and CRN.
- System loads course data for the CRN.
- System creates a formatted `.txt` drop slip.
- Drop slip file includes:
  - student name + ID  
  - CRN + course details  
  - signature line  
  - date line  
- Invalid CRN → “No course found with that CRN.”

---

## 4.6 User Story: Quick Links & Professor Contacts
**As a student, I want fast access to professor contacts and academic resources so that I can find help quickly.**

### Acceptance Criteria
- Student can open a resources menu.
- Menu lists links (e.g., Registrar, Moodle, CPSC Handbook).
- Student can view professor name, email, and office hours.
- Invalid menu selections are handled gracefully.

---


# 5. Use Cases

## 5.1 Use Case: Check Drop Deadline
**Actor:** Student  
**Goal:** Retrieve and view the last day to drop a course for a selected semester.

**Preconditions**
- The student has opened the app.
- The academic calendar has been scraped successfully.

**Main Flow**
1. Student selects “Find Drop Date” from the menu.
2. Student enters the semester name (Fall/Spring/Summer).
3. System loads scraped calendar data.
4. System finds matching semester.
5. System displays the official drop deadline(s).

**Exception Flows**
- If semester is not found → Display “Semester not available.”
- If scraping fails → Display “Could not load calendar data.”

**Acceptance Criteria**
- The correct drop deadline appears for the selected semester.
- The system handles invalid semester input gracefully.

---

## 5.2 Use Case: GPA Calculator
**Actor:** Student  
**Goal:** Allow the student to calculate their GPA using course grades and credit hours.

**Preconditions**
- Student opened GPA calculator.
- Valid grade scale (A–F) is defined.

**Main Flow**
1. Student enters letter grades.
2. Student enters credit hours.
3. System validates grade and hours.
4. System converts letters → quality points.
5. System computes weighted GPA.
6. System displays final GPA (rounded to two decimals).

**Exception Flows**
- Invalid grade → “Invalid grade entered.”
- Missing hours → “Please enter all grades and credit hours.”
- Total hours = 0 → “Cannot compute GPA.”

**Acceptance Criteria**
- GPA is accurate to two decimals.
- Invalid input triggers clear error messages.

---

## 5.3 Use Case: Course Offering Checker
**Actor:** Student  
**Goal:** Check whether a specific course is offered this semester.

**Preconditions**
- Course offering dataset is loaded.
- Student enters a course code (e.g., MATH 2550).

**Main Flow**
1. Student selects “Check if a Course Is Offered.”
2. Student enters course code.
3. System validates input format.
4. System searches current semester offerings.
5. System displays:
   - Offered (sections available)
   - Full (all sections full)
   - Not offered
   - Invalid format

**Exception Flows**
- Incorrect subject/number → “Invalid course format.”
- Course not found → “Course not offered this semester.”

**Acceptance Criteria**
- System correctly classifies course as offered / full / not offered.
- Shows all matching sections when available.

---

## 5.4 Use Case: CRN Lookup
**Actor:** Student  
**Goal:** View CRN, prerequisites, instructor, and add/drop dates for a course.

**Preconditions**
- `courses.csv` data file exists and loads correctly.

**Main Flow**
1. Student selects “CRN Lookup.”
2. Student enters course number or CRN.
3. System loads CSV course data.
4. System finds matching course.
5. System displays CRN, prerequisites, time, days, instructor, and add/drop deadlines.

**Exception Flows**
- Course not found → “No course found with that CRN.”

**Acceptance Criteria**
- All course details are displayed accurately.

---

## 5.5 Use Case: Drop Slip Generator
**Actor:** Student  
**Goal:** Generate an official drop slip text file for a selected CRN.

**Preconditions**
- Student has valid name, ID, and CRN.
- Course exists in CSV.

**Main Flow**
1. Student selects “Create Drop Slip.”
2. Student enters name, ID, term, and CRN.
3. System loads course data.
4. System creates DropSlip object.
5. System generates `drop_slip.txt`.
6. System confirms creation.

**Exception Flows**
- Invalid CRN → “No course found with that CRN.”

**Acceptance Criteria**
- Drop slip file prints correct course + student info.



# 6. Class & Function Design

## 6.1 Class: Course (schedule.py)
**Attributes**
- `crn: str`
- `subject: str`
- `course_number: str`
- `title: str`
- `days: str`
- `time: str`
- `instructor: str`
- `seats_open: int`

**Methods**
- `course_code()` → return "SUBJECT NUMBER"

---

## 6.2 GPA Calculator Module (gpa_calculator.py)
**Functions**
- `convert_grade_to_points(grade)`  
  Converts letter grade → quality points.
- `calculate_gpa(grades, credit_hours)`  
  Computes weighted GPA.
- `run_gpa_calculator()`  
  CLI tool for student entry.

**Test Class**
- `TestGpaCalculator(unittest.TestCase)`

---

## 6.3 Course Offering Checker (course_search.py)
**Functions**
- `search_course_offerings(course_code)`  
  Returns:
  - status (offered/full/not_found/invalid)
  - sections
  - message for UI

**Test Class**
- `TestCourseSearch(unittest.TestCase)`

---

## 6.4 CRN Lookup (crn_check.py)
**Functions**
- `run_crn_lookup()`  
- `load_course_from_csv(crn)`  

**Test Class**
- `TestCRNLookup(unittest.TestCase)`

---

## 6.5 Drop Slip Module (drop_slip.py)
**Class: DropSlip**
- `student_name: str`
- `student_id: str`
- `term: str`
- `course: dict`

**Methods**
- `to_text()` → formatted drop slip text

**Function**
- `write_drop_slip_to_file(slip, filename="drop_slip.txt")`

**Test Class**
- `TestDropSlip(unittest.TestCase)`

---

## 6.6 Schedule Model (schedule.py)
**Class: Schedule**
- `student_id: str`
- `student_name: str`
- `courses: list`

**Methods**
- `add_course(course_dict)`
- `get_courses()`

**Test Class**
- `TestSchedule(unittest.TestCase)`

---

## 6.7 Resources (resources.py)
**Functions**
- `load_default_resources()`
- `get_drop_deadline_info()`
- `load_professor_contacts()`

**Test Class**
- `TestResources(unittest.TestCase)`


# **7. Data Design**

Input Data:
* courses.csv — CRN lookup
* Hardcoded sample course offerings dataset
* Hardcoded professor/contact info

# **8. Test Plan**
| File                     | Covers                      |
| ------------------------ | --------------------------- |
| `test_course_search.py`  | Course offering checker     |
| `test_crn_check.py`      | CRN lookup                  |
| `test_resources.py`      | Resource loading            |
| `test_gpa_calculator.py` | GPA calculator              |
| `test_dropslip.py`       | Drop slip generation        |
| `test_schedule.py`       | Schedule model + CSV loader |



---

# **9. Release Notes**
This final MVP release includes:
* Fully integrated driver with 6 features
* Completed GPA calculator (with tests)
* Course offering checker (with tests)
* CRN lookup (with tests)
* Drop slip generator (with tests)
* Drop deadline scraper
* Professor resource system
* Updated SDD + README
* Working full test suite
* All features accessed from ONE driver command



---

# **10. File Structure**

```
Tsunamis/
│
├── driver.py
├── course_search.py
├── gpa_calculator.py
├── crn_check.py
├── PerformScraping.py
├── drop_slip.py
├── schedule.py
├── resources.py
│
├── data/
│   └── courses.csv
│
├── test/
│   ├── test_course_search.py
│   ├── test_crn_check.py
│   ├── test_resources.py
│   ├── test_gpa_calculator.py
│   ├── test_dropslip.py
│   ├── test_schedule.py
│   └── __pycache__/
│
├── SDD/
│   └── SDD.md
│
└── README.md


---

# **11. Release Notes (Release #1 – MVP)**

### **Completed**
- GPA Calculator implemented  
- Drop deadline function implemented  
- Unit tests added  
- Trello user stories + use cases completed  
- SDD created and uploaded  

### **Next Release Goals**
- Add CRN lookup  
- Add schedule planner  
- Add UI (web or mobile)

---

# **End of Document**
