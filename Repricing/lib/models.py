# account configure class
import os
from lib.utils.config_tool import ConfigTool



class AccountConfig(object):
    def __init__(self, account_code, country, seller_id=None, mws_access_key=None, mws_secret_key=None,
                 mws_auth_token=None):
        self.account_code = account_code
        self.seller_id = seller_id
        self.country = country
        self.mws_access_key = mws_access_key
        self.mws_secret_key = mws_secret_key
        self.mws_auth_token = mws_auth_token

    @staticmethod
    def get(account_code):
        config = ConfigTool()
        config.set_section('account.%s' % account_code.lower())
        seller_id= config.get('seller_id')
        if seller_id is None:
            raise Exception('No configuration for %s found' % account_code)

        country = config.get('country')
        mws_access_key = config.get('mws_access_key')
        mws_secret_key = config.get('mws_secret_key')
        mws_auth_token = config.get('mws_auth_token')
        account_code = account_code

        return AccountConfig(account_code=account_code, country=country, seller_id=seller_id,
                             mws_access_key=mws_access_key, mws_secret_key=mws_secret_key,
                             mws_auth_token=mws_auth_token)
