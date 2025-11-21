from PerformScraping import Scraper

class Driver:

    def main():
        select_soup = Scraper.getAcademicCalander()
        semesterDropDates = Scraper.getDropDates(select_soup)

        print("\nFind the drop date for your semester!")
        usrchoice = input("Which semester are you looking for? (Fall/Spring/Summer): ")
        print("\n")
        

        for key, values in semesterDropDates.items():
            if usrchoice.lower() in key.lower():
                for value in values:
                    print("Drop Dates: ", value)

    
    
    if __name__ == "__main__":
        main()