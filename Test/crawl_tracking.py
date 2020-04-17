import unittest
from crawl_tracking import Usps


class UspsTest(unittest.TestCase):
    def setUp(self):
        self.tracking_number = '9400111899561664217817'
        with open('../data/USPS-Tracking.html', 'r') as html:
            self.usps = Usps(html=html, tracking_number=self.tracking_number)

    def test_status(self):
        self.assertEqual(True, self.usps.get_status())


if __name__ == '__main__':
    unittest.main()
