import time
import sys
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from elasticsearch.exceptions import RequestError
from elasticsearch.exceptions import NotFoundError
from elasticsearch.exceptions import ConnectionTimeout
from elasticsearch.exceptions import ConnectionError
from elasticsearch.exceptions import SSLError
from elasticsearch.exceptions import TransportError
from elasticsearch.exceptions import ElasticsearchException


class OfferService(object):
    def __init__(self, host, port, user, password, max_retry=3):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.max_retry = max_retry
        self.esclient = Elasticsearch(hosts=host, port=port, http_auth=(user, password))

    def get_offers(self, asin_list, country_code='us', condition='Any'):

        if condition.lower() != 'new':
            condition = 'Any'

        params = {
            'index': 'lowest_offer_listings_%s_%s' % (country_code.lower(), condition.lower()),
            'from_': 0, # 从匹配到的结果中的第几条数据开始返回，值是匹配到的数据的下标，从 0 开始
            'size': 500,# 返回多少条数据
            'body': {
                'query': {'terms': {'_id': asin_list}}
            }
        }

        resp = None
        retry = self.max_retry
        while retry > 0:
            # match asins
            try:
                resp = self.esclient.search(**params)
                break
            except NotFoundError as e:
                break
            except RequestError as e:
                raise e
            except ConnectionTimeout:
                time.sleep(1)
            except (TransportError, ElasticsearchException) as e:
                resp = -1
                retry -= 1

                status_code = getattr(e, 'status_code', None)
                if status_code == 'N/A':
                    time.sleep(3)
            except Exception as e:
                resp = -1
                retry -= 1

        if resp is None:
            result = None
        elif resp == -1:
            result = False
        else:
            result = dict()
            for item in resp['hits']['hits']:
                result[item['_id']] = item['_source']

        return result
