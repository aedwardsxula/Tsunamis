# Tsunamis

## What happens when Dr. Edwards runs your code ($ python main.py)

```
Traceback (most recent call last):
  File "/Users/aedwards/ae/Teach/202508/2740/251201_A8_XULA/Tsunamis/driver.py", line 1, in <module>
    from PerformScraping import Scraper
  File "/Users/aedwards/ae/Teach/202508/2740/251201_A8_XULA/Tsunamis/PerformScraping.py", line 1, in <module>
    from bs4 import BeautifulSoup
ModuleNotFoundError: No module named 'bs4'
```

## What happens when Dr. Edwards runs your tests ($ python main.py)

No instructions were provided for how to run your test.


## Final Release Checklist
- [ ] README states purpose, contributors, and how to build, run, and test all the code from the CLI.  Build and run should not assume everyone is using a particular IDE (so don't assume users can click a Run button or use VSC's Command Prompt commands.
- [ ] SDD has the project description, outline, architecture (including UML class diagrams), and all project user stories and use cases.
- [ ] Each team member must update our team's **Statement of Work** shared Excel spreadsheet.  Your grade on this assignment is based ONLY on the quality of your use cases, your GitHub contributions that result in accepted pull requests, and 10% of your grade will be assigned by your fellow team members.
- [*] **Eric** must finish his pushes to our repo by 8 PM on Dec 1st and then check this box.
- [ ] **Tre'sure** must finish her pushes to our repo by 8 PM on Dec 1st and then check this box.
- [√] **Jayce** must finish his pushes to our repo by 8 PM on Dec 1st and then check this box.
- [* ] **Eric** must do one last check that the code builds, runs, and all the tests run by 10 PM on Dec 1st and then check this box.
- [*] **Eric** must "Project Release" tag our repo. 
- [ ] Everyone must complete the Brightspace survey to earn the final points for Assignment08.
- [ ] Everyone should complete the Class Climate survey to help Dr. Edwards improve her teaching.


## Tsunamis Project Priorities (1 = Highest Priority)

1.CPSC Help Desk
2. CPSC Register
3. CPSC Core Curriculum Recommender
4. CPSC Electives
5. CPSC Degree Works
6. CPSC Study Buddies


# How to Run the CPSC Help Desk Project

## Run the application
Before running the application you will first need to install few python libraries. It is best practice to create a virtual environment prior to installing libraries.

Create virtual environment(Optional):
  -python -m venv .venv
  -source .venv/bin/activate

Install necessary libraries:
  -pip install requests
  -pip install bs4

Command to run application:
  -python driver.py

(If on Windows, you may need to use:)
  -py driver.py


## Run all unit tests

Before running the tests you will first need to install few python libraries. It is best practice to create a virtual environment prior to installing libraries. (Skip if you have already done this.)

Create virtual environment(Optional):
  -python -m venv .venv
  -source .venv/bin/activate

Install necessary libraries:
  -pip install requests
  -pip install bs4

Commands to run tests:
  -python -m unittest test.ScraperTest
  -python -m unittest test.test_course_search
  -python -m unittest test.test_crn_check
  -python -m unittest test.test_drop_slip
  -python -m unittest test.test_resources
  -python -m unittest test.test_schedule 


