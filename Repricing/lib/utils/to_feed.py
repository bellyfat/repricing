import datetime
import os

to_feed_file_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'feeds')
if not os.path.isdir(to_feed_file_dir):
    os.makedirs(to_feed_file_dir)


def save_feed_to_file(data, country):
    now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%I")
    file_name = to_feed_file_dir + "/%s-%s.txt" % (country, now)

    with open(file_name, 'w') as filehandle:
        row1 = ['sku','asin','price','quanity']
        filehandle.write('%s\n' % ','.join(row1))

        for listitem in data:
            row = ','.join(listitem)
            filehandle.write('%s\n' % row[:-1])
        filehandle.close()


if __name__ == '__main__':
    data = [['JiuUSBk2016-0620-C09022', 'B01FEOIW0Q', '30.14', '3\n'], ['JiuUSBk2016-0620-C14250', 'B01FEOLGLS', '31.11', '3\n'], ['JiuUSBk2016-0620-C15273', 'B01FEOI7ZQ', '37.49', '3\n'], ['JiuUSBk2016-0620-C40318', 'B01FEOV35W', '211.02', '3\n'], ['JiuUSBk2016-0620-C52982', 'B01FEP0BDG', '44.96', '3\n'], ['JiuUSBk2016-0620-C53510', 'B01FEOVHKI', 69.98, '3\n'], ['JiuUSBk2016-0718-C02212', 'B01FKUIJRA', 29.08, '3\n'], ['JiuUSBk2016-0718-C04075', 'B01A0BISE8', '37.68', '3\n'], ['JiuUSBk2016-0718-C04745', 'B01FJ1RKFC', '34.21', '3\n']]

    save_feed_to_file(data, 'us')




