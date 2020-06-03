from enum import Enum


class ProductType(Enum):
    PRODUCT = 'product'
    CD = 'cd'
    BOOK = 'book'


class ItemCondition(Enum):
    New = 100
    Mint = 90
    LikeNew = 90
    VeryGood = 80
    Good = 70
    Acceptable = 60

    def is_new(self):
        return self.value == 100

    def is_used(self):
        return self.value < 100

    def score(self):
        return self.value


class Country(Enum):
    US = ('USD', 'com', 'ATVPDKIKX0DER', True, 'NA')
    CA = ('CND', 'ca', 'A2EUQ1WTGCTBG2', False, 'NA')
    MX = ('MXD', 'com.mx', 'A1AM78C64UM0Y8', False, 'NA')
    UK = ('GBP', 'co.uk', 'A1F83G8C2ARO7P', True, 'EU')
    FR = ('EUR', 'fr', 'A13V1IB3VIYZZH', False, 'EU')
    DE = ('EUR', 'de', 'A1PA6795UKMFR9', False, 'EU')
    IT = ('EUR', 'it', 'APJ6JRA9NG5V4', False, 'EU')
    ES = ('EUR', 'es', 'A1RKKUPIHCS9HS', False, 'EU')
    JP = ('JPY', 'co.jp', 'A1VC38T7YXB528', False, 'AP')
    AU = ('AUD', 'com.au', 'A39IBJ37TRP1C6', False, 'AP')
    CN = ('CNY', 'cn', 'AAHKV2X7AFYLW', False, 'AP')
    IN = ('INR', 'in', 'A21TJRUUN4KGV', False, 'IN')

    def __init__(self, currency_code, url_postfix, marketplace_id, is_forwarding_source, region):
        self.currency_code = currency_code
        self.url_postfix = url_postfix
        self.marketplace_id = marketplace_id
        self.is_forwarding_source = is_forwarding_source
        self.region = region

    @staticmethod
    def from_code(country_code):
        for country in Country:
            if country.name == country_code.upper():
                return country

        return None

    @property
    def code(self):
        return self.name

    @staticmethod
    def eu_countries():
        return [country for country in Country if country.region == 'EU']

    def is_eu_country(self):
        return self.region == 'EU'

    @staticmethod
    def na_countries():
        return [country for country in Country if country.region == 'NA']

    def is_na_country(self):
        return self.region == 'NA'

    @staticmethod
    def ap_countries():
        return [country for country in Country if country.region == 'AP']

    def is_ap_country(self):
        return self.region == 'AP'

    @staticmethod
    def forwarding_sources():
        return [country for country in Country if country.is_forwarding_source]

    def base_url(self):
        return 'https://www.amazon.%s' % self.url_postfix
