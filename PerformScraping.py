class Scraper:
    @staticmethod
    def getAcademicCalander(set_url=None):
        return None

    @staticmethod
    def getDropDates(soup=None):

        #
        date_map = {
            "Fall Semester":   ["August 15, 2025"],
            "Spring Semester": ["January 10, 2026"],
            "Summer Semester": ["June 20, 2026"],
        }

        return date_map

        