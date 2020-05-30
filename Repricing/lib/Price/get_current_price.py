from lib.Inventory_report_lines import Line


def get_current_price(lines):
    current_price = {}
    for line in lines:
        a = Line(line)
        price = a.price
        sku = a.sku
        current_price[sku] = price
    return current_price

