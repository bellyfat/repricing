import sys
import unittest
sys.path.append('..')
from repricing import sku_source_price


class MyTestCase(unittest.TestCase):
    def test_sku_source_price(self):
        lines = ['JiuUSBk2016-0620-C09022,B01FEOIW0Q,30.14,3', 'JiuUSBk2016-0620-C14250,B01FEOLGLS,31.11,3', 'JiuUSBk2016-0620-C15273,B01FEOI7ZQ,37.49,3']
        source_price = {'0394527658': 5.7, '0826701442': 7.96, '0781756529': 8.29}
        self.assertEqual(sku_source_price(lines, source_price),
                         {'JiuUSBk2016-0620-C09022': 5.7, 'JiuUSBk2016-0620-C14250': 7.96,
                          'JiuUSBk2016-0620-C15273': 8.29})


if __name__ == '__main__':
    unittest.main()
