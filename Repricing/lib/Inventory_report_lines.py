import json

import requests


class Line(object):
    def __init__(self, line, fake=None, condition=None, product_type=None, country=None):
        namesList = line.split(",")
        self.sku = namesList[0]
        self.asin = namesList[1]
        self.price = namesList[2]
        self.quantity = namesList[3]
        self.fake = fake
        self.condition = condition
        self.product_type = product_type
        self.country = country

    @staticmethod
    def get_isbn(asin):
        listing_mapping_base_url = 'http://35.199.3.83/listing-mapping/doc/'
        listing_mapping_url = listing_mapping_base_url + asin
        resp = requests.get(listing_mapping_url)
        resp_dict = json.loads(resp.text)
        isbn = resp_dict['_source']['isbn']
        return isbn


if __name__ == '__main__':
    lines = ['JiuUSBk2016-0620-C09022,B01FEOIW0Q,30.14,3', 'JiuUSBk2016-0620-C14250,B01FEOLGLS,31.11,3',
             'JiuUSBk2016-0620-C15273,B01FEOI7ZQ,37.49,3']
    for line in lines:
        a = Line(line)
        sku = a.sku
        print(sku)
