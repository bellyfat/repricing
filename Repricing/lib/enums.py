from enum import Enum


class ProductType(Enum):
    PRODUCT = 'product'
    CD = 'cd'
    BOOK = 'book'


class ItemCondition(Enum):
    NEW = 'New'
    ANY = 'Any'


class SubCondition(Enum):
    NEW = 'New'
    VeryGood = 'Very good'
    LikeNew = 'Like new'
    Good = 'Good'


class CountryCode(Enum):
    US = 'us'
    UK = 'uk'
    CA = 'ca'
    FR = 'fr'
    IT = 'it'
    ES = 'es'
    DE = 'de'
