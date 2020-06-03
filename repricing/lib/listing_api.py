import csv
import datetime
from six import ensure_text,StringIO
from lib.models import AccountConfig
from mws_wrapper.mws_report import MWSReportApi


class ListingApi(object):
    def __init__(self,account_config:AccountConfig,report_file_path):
        self.report_file_path = report_file_path
        self.account_config = account_config
        self.report_api = MWSReportApi(self.account_config.country.upper(), account_config.seller_id,
                                       account_config.mws_access_key,
                                       account_config.mws_secret_key,
                                       auth_token=account_config.mws_auth_token)
        
    def get_inventory_report(self, country=None):
        return self.get_report('_GET_FLAT_FILE_OPEN_LISTINGS_DATA_', country)

    def get_report(self, report_type, country=None, save_to_file=True):
        if country is None:
            country = self.account_config.country.upper()

        report_data = self.report_api.get_report(report_type, country=country)
        if save_to_file:
            return self.save_report_to_file(report_data, report_type, country)

        return report_data

    def save_report_to_file(self, data, report_type, country):
        now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%I")
        file_name = self.report_file_path + "/%s-%s-%s.csv" % (report_type, country, now)

        w = open(file_name, "w")
        writer = csv.writer(w, delimiter=',')

        if isinstance(data, bytes):
            data = ensure_text(data)

        f = StringIO(data)

        reader = csv.reader(f, delimiter="\t")

        index = 0
        for row in reader:
            index = index + 1
            writer.writerow(row)
        w.close()

        return file_name
