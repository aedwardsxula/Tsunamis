import unittest
import requests
from unittest.mock import patch, MagicMock
from help_desk.resources import Resource, load_default_resources


class TestResources(unittest.TestCase):

    def link_requests(url: str):
        try:
            response = requests.head(url, timout=10)
            if(response.status_code == 200):
                return True
        except:
            return False


    def test_returns_list(self):
        resources = load_default_resources()

        self.assertIsInstance(resources, list)
    
    def test_resource_count(self):
        resources = load_default_resources()

        self.assertEqual(len(resources), 4)

    def test_items_are_resources(self):
        resources = load_default_resources()

        for item in resources:
            self.assertIsInstance(item, Resource)
    
    def test_resource_fields(self):
        resources = load_default_resources()

        firstResource = resources[0]

        self.assertEqual(firstResource.name, "XULA Academic Calendar")
        self.assertEqual(firstResource.url, "https://www.xula.edu/academics/calendar")
        self.assertEqual(firstResource.category, "Academics")
        self.assertEqual(firstResource.icon, "calendar")
    
    @patch("requests.head")
    def test_functional_links(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        resources = load_default_resources()
        test_link = ""

        for item in resources:
            test_link = item.url
            self.assertTrue(TestResources.link_requests(test_link))

    @patch("requests.head")
    def test_nonfunctional_links(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        self.assertFalse(TestResources.link_requests("https://invalid-url#"))
           
if __name__ == "__main__":
    unittest.main()


