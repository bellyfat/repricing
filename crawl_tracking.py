import requests
from bs4 import BeautifulSoup

from lib.utils import get_Usps_html_from_url


class Tracking(object):
    tracking_number = None

    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')

    def get_status(self):
        status_tag_text = None
        status_tag = self.soup.select(".delivery_status")
        for p in status_tag:
            text = p.get_text().strip()
            status_tag_text = ''.join(text)
        return (status_tag_text)
        # if "Delivered" is in status_tag_text:
        #     return ("Delivered")


if __name__ == "__main__":
    tracking_number = "9400111899561664217817"
    html = get_Usps_html_from_url(tracking_number)
    usps = Tracking(html)
    print(usps.get_status())
