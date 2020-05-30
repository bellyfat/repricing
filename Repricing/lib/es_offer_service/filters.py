from lib import logger


class OfferFilter(object):
    def __init__(self, **kw):
        self.dict_subcondition = {
            'new': 100,
            'mint': 90,
            'very_good': 81,
            'verygood': 80,
            'good': 70,
            'acceptable': 60,
            'poor': 50,
            'club': 40,
            'oem': 30,
            'warranty': 25,
            'refurbishedwarranty': 20,
            'refurbished_warranty': 21,
            'refurbished': 15,
            'open_box': 10,
            'openbox': 11,
            'Other': 0
        }

        self.filter = {
            'rate': 90,
            'review': 100,
            'domestic': None,
            'shipping_time': 2,
            'subcondition': 70,
            'fba': None
        }

        for key in kw:
            if key in self.filter:
                self.filter[key] = kw[key]

    def get_filtered_offers(self, offer_listings, condition='any'):
        filtered_offers = []

        if len(offer_listings) <= 0:
            logger.debug('[NoOfferFound] %s - %s' % (offer_listings, self.filter))
            return filtered_offers

        for offer_listing in offer_listings:
            fba = offer_listing['fba']
            offer_condition = offer_listing['condition']
            # print fba, offer_condition, offer_listing

            if condition.lower() == 'new' and offer_condition.lower() != 'new':
                continue

            # fba
            if self.filter['fba'] is not None and fba != self.filter['fba']:
                continue

            ships_domestically = offer_listing['domestic']
            if self.filter['domestic'] is not None and ships_domestically != self.filter['domestic']:
                continue

            shipping_time = offer_listing['shipping_time']
            if shipping_time is not None and fba is False:

                if shipping_time['min'] > self.filter['shipping_time']:
                    continue

            rating = offer_listing['rating']
            if rating['min'] < self.filter['rate'] and fba is False:
                continue

            feedback_count = offer_listing['feedback']
            if feedback_count < self.filter['review'] and fba is False:
                continue

            subcondition = offer_listing['subcondition']
            if self.dict_subcondition[subcondition.lower()] < self.filter['subcondition']:
                continue

            filtered_offers.append(offer_listing)

        if len(filtered_offers) > 0:
            filtered_offers_str = [str(filtered_offer) for filtered_offer in filtered_offers]
            logger.debug('[FilteredOffer] %s - %s' % ("\n".join(filtered_offers_str), self.filter))

        return filtered_offers

    def get_lowest_priced_filtered_offer(self, lowest_offer_listing, condition='any'):
        lowest_priced_offer = None

        filtered_offers = self.get_filtered_offers(lowest_offer_listing, condition)
        if len(filtered_offers) <= 0:
            return lowest_priced_offer

        for offer in filtered_offers:
            if lowest_priced_offer is None:
                lowest_priced_offer = offer
                continue

            price1 = self.calc_offer_price(lowest_priced_offer)
            price2 = self.calc_offer_price(offer)
            if price1 > price2:
                lowest_priced_offer = offer

        lowest_priced_offer.set_offers(len(filtered_offers))
        return lowest_priced_offer

    def get_lowest_priced_filtered_offers(self, lowest_offer_listing, condition='any', count=3):
        lowest_priced_offer = None

        filtered_offers = self.get_filtered_offers(lowest_offer_listing, condition)
        if len(filtered_offers) <= 0:
            return lowest_priced_offer

        filtered_offers.sort(key=lambda o: self.calc_offer_price(o))  # sorts in place
        if len(filtered_offers) > count:
            filtered_offers = filtered_offers[0:count]

        offers = []
        for offer in filtered_offers:
            offers.append(offer)
        return offers

    def sort_offer_by_price(self, lowest_offer_listing):
        sorted_offer_listing = []
        offer_listings = lowest_offer_listing.get_offer_listings()
        if len(offer_listings) <= 0:
            return sorted_offer_listing

        offer_listings.sort(key=self.calc_offer_price)

        return offer_listings

    @staticmethod
    def calc_offer_price(offer):
        return offer['price']
