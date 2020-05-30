import json

from lib.es_offer_service.filters import OfferFilter
from lib.es_offer_service.offer_service import OfferService
from lib.es_offer_service.offer_service_price_finder import OfferServicePriceFinder

if __name__ == '__main__':
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
    # asins = ['0394527658','0826701442','0781756529','1481859579']
    asins = ['0394527658']
    source_country = 'us'
    condition = 'any'
    offers = offer_finder.find_offer_for_asins(asins, source_country, condition)
    print(offers)
