import json
from datetime import datetime
from cmutils.currency_mapping import CurrencyMapping
from elasticsearch.exceptions import RequestError
from lib import set_logger_handler


def list_unique(l):
    """Return a new list with duplicate items removed, not reserve order
    """
    return list({}.fromkeys(l).keys())


class OfferServicePriceFinder(object):
    def __init__(self, offer_service, offer_filter, log_file=None, offer_alive_hours=48):
        self.offer_alive_hours = offer_alive_hours
        if log_file is None:
            log_file = 'offer_service_price_finder.log'
        self.logger = set_logger_handler(log_file)

        # Setup offer service
        self.offer_service = offer_service
        self.offer_filter = offer_filter

    def search_offers(self, query, country='us', condition='Any', size=500, offset=0, sort=None):
        offers = dict()
        try:
            offers_info = self.offer_service.search_offers(query, country, condition, size, offset, sort)

            if offers_info is None:
                offers = None
            elif offers_info == -1:
                offers = False
            else:
                offers = self._parse_service_offers(offers_info)
        except RequestError as e:
            self.logger.warn(
                '[ElasticSearchRequestError] message: %s, info: %s', e.error, str(e.info))

        return offers

    def find_offer_for_asins(self, asins, country, condition):
        condition = condition.lower()
        """
        Returns:
          None - Not found on elastic search server
          False - Elastic search unavailable or could not connect to elastic search
          dict - Result on elastic search
        """
        offers = dict()

        asins = list_unique(asins)
        if len(asins) <= 0:
            return offers

        try:
            offers_info = self.offer_service.get_offers(asins, country, condition)
            # print country,condition,asins,offers_info
            if offers_info is None:
                offers = None
            elif offers_info == -1:
                offers = False
            else:
                offers = self._parse_service_offers(offers_info, condition)
                for asin in asins:
                    offers.setdefault(asin, None)
        except RequestError as e:
            self.logger.warn(
                '[ElasticSearchRequestError] message: %s, info: %s', e.error, str(e.info))

        return offers

    def _parse_service_offers(self, offers_info, condition):
        offers = dict()
        if len(offers_info) <= 0:
            return offers
        for key, value in offers_info.items():

            # Set offer to expired when no time field exist or time value is invalid
            if 'time' not in value:
                expired = True
            else:
                try:
                    offer_time = datetime.strptime(value['time'][:19], '%Y-%m-%dT%H:%M:%S')
                    now = datetime.utcnow()
                    diff_seconds = (now - offer_time).total_seconds()
                    expired = diff_seconds > 3600 * self.offer_alive_hours
                except ValueError:
                    expired = True

            lowest_offers = json.loads(value['offers'])
            loffers = self.offer_filter.get_lowest_priced_filtered_offers(lowest_offers, condition)
            if loffers is None:
                continue

            offer = loffers[0]
            offers[key] = offer
            offers[key]['_from'] = 'service'
            offers[key]['currency'] = CurrencyMapping.get_currency(offer['country'])
            offers[key]['expired'] = expired

            # Set offer to out of stock when value is incomplete
            try:
                offers[key]['product_price'] = float(offer['product_price'])
                offers[key]['shipping_price'] = float(offer['shipping_price'])
                offers[key]['price'] = \
                    offers[key]['product_price'] + offers[key]['shipping_price']
            except Exception as e:
                self.logger.warn('[OfferServerParseError] %s', value)
                self.logger.exception(e)
                offers[key]['has_offer'] = 'n'
                offers[key]['offers'] = 0

        return offers
