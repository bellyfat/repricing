from lib.closing_fee import ClosingFee


def get_min_price(source_price, min_profit_amount, min_profit_rate, type='book', marketplace='us'):
    if type != 'product':
        closing_fee = ClosingFee.get_closing_fee(marketplace)

    min_price_by_rate = (source_price + min_profit_amount + closing_fee) / 0.85
    min_price_by_amount = (source_price * (1 + min_profit_rate)) / 0.85
    min_price = max(min_price_by_rate, min_price_by_amount)
    return min_price


# match [sku, min_price]
def sku_min_price(sku_source_price, min_profit_amount, min_profit_rate):
    sku_min_price = {}
    for key in sku_source_price:
        if sku_source_price[key] is not None:
            price = get_min_price(sku_source_price[key], min_profit_amount, min_profit_rate)
            sku_min_price[key] = price
        else:
            sku_min_price[key] = 0
    return sku_min_price
