# resources.py
from dataclasses import dataclass
from typing import List
from pathlib import Path
import json

@dataclass
class Resource:
    name: str
    url: str
    category: str
    icon: str  

def load_default_resources() -> List[Resource]:
    """Return a list of common XULA/CPSC resource links."""
    return [
        Resource(
            name="XULA Academic Calendar",
            url="https://www.xula.edu/academics/calendar",
            category="Academics",
            icon="calendar"
        ),
        Resource(
            name="Drop Deadline Calendar",
            url="https://www.xula.edu/registrar",
            category="Academics",
            icon="deadline"
        ),
        Resource(
            name="CRN Tools",
            url="https://selfservice.xula.edu",
            category="Courses",
            icon="tools"
        ),
        Resource(
            name="CPSC Tutoring Info",
            url="https://www.xula.edu/computer-science",
            category="Tutoring",
            icon="tutor"
        ),
    ]

def get_drop_deadline_info() -> str:
    """
    Returns the drop deadline information.
    """
    return (
        "Drop Deadline Information:\n"
        "- Last day to drop a course: Sept 15\n"
        "- Last day to withdraw with a 'W': Oct 27\n"
        "(Check XULA Registrar for official updates)"
    )
def load_professor_contacts() -> dict:
    """Return professor contact info for common CPSC courses."""
    return {
        "CPSC 1710": {
            "professor": "Dr. Edwards",
            "email": "edwards@xula.edu",
            "office_hours": "MWF 1–3PM"
        },
        "CPSC 2735": {
            "professor": "Dr. Lanf",
            "email": "lang@xula.edu",
            "office_hours": "TR 10–12PM"
        },
        "CPSC 3350": {
            "professor": "Dr. Hayes",
            "email": "hayes@xula.edu",
            "office_hours": "MW 2–4PM"
        }
    }
DATA_FILE = Path("data") / "resources.json"

def load_resources_from_json() -> List[Resource]:
    """Load resource links from JSON file."""
    if not DATA_FILE.exists():
        raise FileNotFoundError("resources.json not found.")

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)

    return [Resource(**item) for item in raw]
