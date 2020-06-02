from lib.enums import ProductType, SubCondition, ItemCondition, CountryCode


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
        data.update(condition)
        data.update({'product_type': product_type, 'source': source, 'zd': zd})
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
        if cls.parse_type(sku) == ProductType.PRODUCT:
            return {'item_condition': ItemCondition.NEW, 'sub_condition': SubCondition.NEW}

        if ("new" in sku.lower()) or ("xin" in sku.lower()) or (sku.lower()[:1] == 'n'):
            return {'item_condition': ItemCondition.NEW, 'sub_condition': SubCondition.NEW}

        if 'vg' in sku.lower():
            return {'item_condition': ItemCondition.ANY, 'sub_condition': SubCondition.VeryGood}

        if 'ln' in sku.lower():
            return {'item_condition': ItemCondition.ANY, 'sub_condition': SubCondition.LikeNew}

        return {'item_condition': ItemCondition.ANY, 'sub_condition': SubCondition.Good}

    @classmethod
    def parse_source(cls, sku, country_code):
        sku = sku.replace('_', '-').lower()
        if sku.replace("used", "").lower().find("us") >= 0:
            return CountryCode.US

        if sku.lower().find("uk") >= 0:
            return CountryCode.UK

        if country_code.lower() in sku:
            return country_code

        return CountryCode.US


if __name__ == '__main__':
    sku = 'usedzd-ukbook-191114-c049530'
    print(SkuParser.parser_sku(sku, 'uk'))
