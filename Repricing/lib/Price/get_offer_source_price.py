import os

from lib.Inventory_report_lines import Line
from lib.es_offer_service.offer_service import OfferService
from lib.es_offer_service.filters import OfferFilter
from lib.es_offer_service.offer_service_price_finder import OfferServicePriceFinder
from lib.utils.read_inventory_report_tool import new_report, read_file_by_size


# match [sku,source_price]
def get_source_price(lines):
    offer_service = OfferService('35.245.123.47', 80, 'elasticuser', 'KbersRiseUp153')
    filter_cond = {
        'rate': 80,
        'review': 50,
        'domestic': True,
        'shipping_time': 5,
        'subcondition': 70
    }

    offer_filter = OfferFilter(**filter_cond)
    offer_finder = OfferServicePriceFinder(offer_service=offer_service, offer_filter=offer_filter)
# get isbns from lines
    isbns_dic = {}
    for line in lines:
        a = Line(line)
        asin = a.asin
        isbns_dic[asin] = a.get_isbn(asin)
    isbns = list(isbns_dic.values())
# get source_price from es price offer
    asins = isbns
    source_country = 'us'
    condition = 'any'
    offers = offer_finder.find_offer_for_asins(asins, source_country, condition)
    source_price = {}
    for asin in asins:
        if offers[asin] is not None:
            source_price[asin] = offers[asin].get('price')
        else:
            source_price[asin] = None
# match [sku,source_price]
    sku_source_price = {}
    for line in lines:
        a = Line(line)
        sku = a.sku
        asin = a.asin
        isbn = a.get_isbn(asin)
        sku_source_price[sku] = source_price[isbn]
    return sku_source_price


if __name__ == '__main__':
    file_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + '/reports'
    new_report = new_report(file_path)
    lines = read_file_by_size(new_report, 5)
    sku_source_price = get_source_price(lines)
    print(sku_source_price)
