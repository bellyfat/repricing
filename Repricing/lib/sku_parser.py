class SkuParser(object):
    @classmethod
    def parser_sku(cls, sku):

        data = {}
        condition = cls.parse_condition(sku)
        product_type = cls.prase_type(sku)
        country = cls.parse_source(sku)
        zd = cls.parse_zd(sku)
        data[sku] = {condition, product_type, country, zd}
        return data

    @classmethod
    def parse_source(cls,sku):
        if 'US'in sku.upper():
            source = 'us'
        return source

    @classmethod
    def parse_type(cls, sku):
        if 'BK' in sku.upper():
            product_type = 'book'
        elif 'P' in sku.upper():
            product_type ='product'
        return product_type

    @classmethod
    def parse_zd(cls, sku):
        return sku.lower().find('zd') > 0

    @classmethod
    def parse_condition(cls, sku):
        if 'new' or 'xin' or 'mint' or 'brand_new' in sku.lower():
            condition = 'New'
        else:
            condition = 'Any'
        return condition
