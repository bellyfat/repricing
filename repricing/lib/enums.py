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
    US = ('USD', 'com', 'ATVPDKIKX0DER', True)
    CA = ('CND', 'ca', 'A2EUQ1WTGCTBG2', False)
    MX = ('MXD', 'com.mx', 'A1AM78C64UM0Y8', False)
    UK = ('GBP', 'co.uk', 'A1F83G8C2ARO7P', True)
    FR = ('EUR', 'fr', 'A13V1IB3VIYZZH', False)
    DE = ('EUR', 'de', 'A1PA6795UKMFR9', False)
    IT = ('EUR', 'it', 'APJ6JRA9NG5V4', False)
    ES = ('EUR', 'es', 'A1RKKUPIHCS9HS', False)
    JP = ('JPY', 'co.jp', 'A1VC38T7YXB528', False)
    AU = ('AUD', 'com.au', 'A39IBJ37TRP1C6', False)
    CN = ('CNY', 'cn', 'AAHKV2X7AFYLW', False)
    IN = ('INR', 'in', 'A21TJRUUN4KGV', False)

    def __init__(self, currency_code, url_postfix, marketplace_id, is_forwarding_source):
        self.currency_code = currency_code
        self.url_postfix = url_postfix
        self.marketplace_id = marketplace_id
        self.is_forwarding_source = is_forwarding_source

    @staticmethod
    def from_code(country_code):
        for country in Country:
            if country.name == country_code.upper():
                return country

        return None

    def base_url(self):
        return 'https://www.amazon.%s' % self.url_postfix

    @property
    def code(self):
        return self.name

    @property
    def eu_countries(self):
        return [self.UK, self.DE, self.FR, self.ES, self.IT]

    def is_eu_country(self):
        return self in self.eu_countries

    @staticmethod
    def forwarding_sources():
        return [country for country in Country if country.is_forwarding_source]


if __name__ == '__main__':
    print(Country.UK.is_eu_country())
    print(Country.US.is_eu_country())
    print(Country.from_code('uk'))
