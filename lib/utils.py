import requests

USPS_Hard_link = "https://tools.usps.com/go/TrackConfirmAction?tRef=fullpage&tLc=2&text28777=&tLabels="
DHL_Hard_link = "https://www.dhl.com/global-en/home/tracking/tracking-ecommerce.html?submit=1&tracking-id="
Fedex_Hard_link = "https://www.fedex.com/apps/fedextrack/?action=track&tracknumbers="
OSM_Hard_link = "https://www.osmworldwide.com/tracking/?trackingNumbers="
UPS_Hard_link = "https://www.ups.com/track?loc=en_US&tracknum="


def get_Usps_html_from_url(tracking_number):
    url = USPS_Hard_link + tracking_number
    s = requests.Session()
    s.headers[
        'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    return s.get(url).text
