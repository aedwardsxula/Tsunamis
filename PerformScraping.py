from bs4 import BeautifulSoup
import requests

class Scraper:

    def getAcademicCalander(set_url=None):
        if(set_url == None):
            url =  "https://www.xula.edu/academics/academiccalendar/index.html"
        else:
            url = set_url
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        if response.status_code == 200:
            return soup
        else:
            print("Could not find page")

    def getDropDates(soup):
            target_text = "Last Day to Drop a Course"
            date = ""
            dropList = []
            fallMonths = ["September", "October", "November", "December"]
            springMonths = ["January", "February", "March", "April"]
            summerMonths = ["May", "June", "July", "August"]
            date_map = { }

            titles = soup.find_all("tr")
            for row in titles:
                cells = row.find_all("td")
                if cells:
                    first_col = cells[0].text.strip().lower()
                    if(target_text.lower() in first_col):
                        date = cells[1].text.strip()
                        if date:
                            dropList.append(date)
            
            for c in dropList:
                month = c.split()[0]
                if(month in fallMonths):
                    date_map.setdefault("Fall Semester",[]).append(c)
                elif(month in springMonths):
                    date_map.setdefault("Spring Semester",[]).append(c)
                elif(month in summerMonths):
                    date_map.setdefault("Summer Semester",[]).append(c)
                 
            
            return date_map

    

        