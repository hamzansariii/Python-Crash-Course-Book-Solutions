import unittest
from city_functions import City_Country_Name


class test_City_Country_Name(unittest.TestCase):
    '''This class will test the name of city and country'''

    def test_cityname_countryname(self):
        name = City_Country_Name("santiago", "chile", "population=50000")
        self.assertEqual(name,  "santiago,chile,population=50000")


if __name__ == '__main__':
    unittest.main()
