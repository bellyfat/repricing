from repricing.lib.enums import ProductType, ItemCondition, Country
from repricing.lib.utils.str_utils import contains_any_ignorecase


class UnknownProductTypeException(Exception):
    pass


class SkuParser(object):
    @classmethod
    def parser_sku(cls, sku, country_code='uk'):
        data = {}
        condition = cls.parse_condition(sku)
        source = cls.parse_source(sku, country_code)
        zd = cls.parse_zd(sku)
        product_type = cls.parse_type(sku)
        data.update({'product_type': product_type, 'source': source, 'zd': zd, 'condition': condition})
        return data

    @classmethod
    def parse_type(cls, sku):
        sku = sku.replace('_', '-')
        code = sku.lower().split("-")[-1][:1]

        if code == 'c':
            return ProductType.BOOK

        if code == 'g':
            return ProductType.CD

        if code == 'p':
            return ProductType.PRODUCT

        raise UnknownProductTypeException("Unknown product code %s" % code)

    @classmethod
    def parse_zd(cls, sku):
        return sku.lower().find('zd') > 0

    @classmethod
    def parse_condition(cls, sku):
        sku = sku.lower()

        if cls.parse_type(sku) == ProductType.PRODUCT:
            return ItemCondition.New

        if contains_any_ignorecase(sku, ['new', 'xin']) or sku.startswith('n'):
            return ItemCondition.New

        if 'vg' in sku:
            return ItemCondition.VeryGood

        if 'ln' in sku:
            return ItemCondition.LikeNew

        return ItemCondition.Good

    @classmethod
    def parse_source(cls, sku, marketplace_country):

        if isinstance(marketplace_country, str):
            marketplace_country = Country.from_code(marketplace_country)

        sku = sku.lower().replace("used", "")
        for country in Country.forwarding_sources():
            if contains_any_ignorecase(sku, country.name):
                return country

        if contains_any_ignorecase(sku, marketplace_country.name):
            return marketplace_country

        return Country.US


if __name__ == '__main__':
    sku = 'usedzd-ukbook-191114-c049530'
    print(SkuParser.parser_sku(sku, 'uk'))
