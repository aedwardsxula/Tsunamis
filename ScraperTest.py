import unittest
import requests
from PerformScraping import Scraper
from bs4 import BeautifulSoup
from unittest.mock import patch, MagicMock

class ScaperTest(unittest.TestCase):

    @patch('PerformScraping.requests.get')
    def test_getAcademicCalander_success(self,mock_get):
        url = "https://sample.com"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "<html><head><title>Academic Calendar</title></head></html>"
        mock_get.return_value = mock_response

        soup = Scraper.getAcademicCalander(url)

        self.assertIsInstance(soup, BeautifulSoup)
        self.assertEqual(soup.text, "Academic Calendar")

    @patch('PerformScraping.requests.get')
    def test_getAcademicCalander_no_url_provided(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "<html><head><title>Academic Calendar</title></head></html>"
        mock_get.return_value = mock_response

        soup = Scraper.getAcademicCalander()

        self.assertIsInstance(soup, BeautifulSoup)

    @patch('PerformScraping.requests.get')
    def test_getAcademicCalander_invalid_url(self, mock_get):
        url = "https://invalid-url"
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.text = ""
        mock_get.return_value = mock_response

        soup = Scraper.getAcademicCalander(url)

        self.assertIsNone(soup)
    
    def test_getDropDates_succes(self):
        Mock_HTML = """
            <table>
                <tr><td>Last Day to Drop A Course</td><td>January 22</td></tr>
                <tr><td>Last Day to Drop A Course Without a W</td><td>October 2</td></tr>   
                <tr><td>Last Day to Drop A Course</td><td>July 12</td></tr>   
            </table>       
        """
        soup = BeautifulSoup(Mock_HTML, "html.parser")
        results = Scraper.getDropDates(soup)

        expected = {
            "Fall Semester": ["October 2"],
            "Spring Semester": ["January 22"],
            "Summer Semester": ["July 12"]
        }

        self.assertEqual(results, expected)
    
    def test_getDropDates_invalid_rows(self):
        Mock_HTML = """
            <table>
                <tr><td>Last Day to Drop A Course</td><td>January 22</td></tr>
                <tr><td>Last Day to Drop A Course Without a W</td><td>LLL?&LL</td></tr>   
                <tr><td>Last Day to Drop A Course</td><td>July 12</td></tr>   
                <tr><td>Last Day to Drop A Course Without a W</td><td>August 8</td></tr>
            </table>       
        """
        soup = BeautifulSoup(Mock_HTML, "html.parser")
        results = Scraper.getDropDates(soup)

        expected = {
            "Spring Semester": ["January 22"],
            "Summer Semester": ["July 12", "August 8"]
        }

        self.assertEqual(results, expected)
        
if __name__=='__main__':
    unittest.main()