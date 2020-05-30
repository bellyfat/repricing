import os
import click
from lib.models import AccountConfig
from lib.listing_api import ListingApi


reports_file_dir = os.path.join(os.path.dirname(__file__), 'reports')
if not os.path.isdir(reports_file_dir):
    os.makedirs(reports_file_dir)


# give account_name, get inventory report

# 1.get configure information from configuration file,include api information
# @click.command('Download and process listing via mws api')
# @click.option('-a', '--account_code', required=True, help='Account SID')
# @click.option('-c', '--country', type=str, default=None, help='country of the inventory')
# @click.option('-t', '--report_type', type=str, default="inventory", help='report type: inventory,inactive,active,all')
# @click.option('-f', '--report_file', type=str, default=None, help='File')
def run(account_code, report_type='inventory', country=None, report_file=None):
    account_config = AccountConfig.get(account_code)
    if report_file is not None:
        report_file = reports_file_dir + '/' + report_file

    listing_api = ListingApi(account_config, reports_file_dir)
    if report_type == 'inventory':
        if report_file is None:
            report_file = listing_api.get_inventory_report(country)


if __name__ == "__main__":
    run('742uk')
