class ClosingFee(object):
    """
    Mapping amazon closing fee for each marketplace.
    """
    closing_fees = {
        'US': 1.8,
        'EU': 0.49,
        'CA': 1,
        'JP': 0.49,
        'MX': 1,
        'CN': 7
    }

    @classmethod
    def get_closing_fee(cls, marketplace):
        """
        Return closing fee for marketplace
        """
        cc = marketplace.upper()
        if cc in ['UK', 'DE', 'ES', 'FR', 'IT']:
            cc = 'EU'

        if cc in cls.closing_fees:
            return cls.closing_fees[cc]

        return 0
