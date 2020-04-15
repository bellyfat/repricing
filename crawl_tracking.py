import requests
from bs4 import BeautifulSoup

USPS_Hard_link = "https://tools.usps.com/go/TrackConfirmAction?tRef=fullpage&tLc=2&text28777=&tLabels="
DHL_Hard_link = "https://www.dhl.com/global-en/home/tracking/tracking-ecommerce.html?submit=1&tracking-id="
Fedex_Hard_link = "https://www.fedex.com/apps/fedextrack/?action=track&tracknumbers="
OSM_Hard_link = "https://www.osmworldwide.com/tracking/?trackingNumbers="
UPS_Hard_link = "https://www.ups.com/track?loc=en_US&tracknum="


# Other_Hard_link="https://www.fedex.com/apps/fedextrack/?action=track&tracknumbers="


class USPS(object):
    USPS_Hard_link = "https://tools.usps.com/go/TrackConfirmAction?tRef=fullpage&tLc=2&text28777=&tLabels="
    tracking_number = None

    def __init__(self, tracking_number):
        self.tracking_number = tracking_number

    def get_webpage(self):
        Base_url = USPS_Hard_link + self.tracking_number
        s = requests.Session()
        s.headers[
            'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        html = s.get(Base_url).text
        webpage = BeautifulSoup(html, 'html.parser')
        return webpage

    def get_status(self, html):
        status_tag_text = None
        status_tag = html.select(".delivery_status")
        for p in status_tag:
            text = p.get_text().strip()
            status_tag_text = ''.join(text)
        return (status_tag_text)
        # if "Delivered" is in status_tag_text:
        #     return ("Delivered")


if __name__ == "__main__":
    tracking_number = "9400111899561664217817"
    usps = USPS(tracking_number)
    html = usps.get_webpage()
    print(usps.get_status(html)
          )
