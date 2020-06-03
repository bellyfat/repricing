import os

from lib.Inventory_report_lines import Line
from lib.Price.get_current_price import get_current_price
from lib.Price.cal_min_price import sku_min_price
from lib.Price.get_offer_source_price import get_source_price
from lib.utils.read_inventory_report_tool import new_report, read_file_by_size
from lib.utils.to_feed import save_feed_to_file


def compete_price(lines, current_price, sku_min_price):
    to_price = []
    for line in lines:
        a = Line(line)
        sku = a.sku
        if float(current_price[sku]) < float(sku_min_price[sku]):
            a.price = str(float('%.2f' % sku_min_price[sku]))
        feed_line = [a.sku, a.asin, a.price, a.quantity]
        to_price.append(feed_line)
    return to_price


if __name__ == '__main__':
    min_profit_rate = 1  # for book
    min_profit_amount = 2.0  # for book

    # read download inventory report
    file_path = os.path.abspath(os.path.dirname(__file__)) + '/reports'
    new_report = new_report(file_path)
    lines = read_file_by_size(new_report, 50)

    sku_source_price = get_source_price(lines)

    sku_min_price = sku_min_price(sku_source_price, min_profit_amount, min_profit_rate)

    current_price = get_current_price(lines)

    to_price = compete_price(lines, current_price, sku_min_price)
    print(to_price)
    save_feed_to_file(to_price, 'us')