import sys
import logging

import os
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('account_assistant.' + __name__)
formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

blacklist_local_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
if not os.path.exists(blacklist_local_dir):
    os.mkdir(blacklist_local_dir)

feeds_file_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'feeds')
if not os.path.isdir(feeds_file_dir):
    os.makedirs(feeds_file_dir)

reports_file_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'reports')
if not os.path.isdir(reports_file_dir):
    os.makedirs(reports_file_dir)


def set_logger_handler(log_file_name):
    work_dir = os.path.dirname(os.path.dirname(__file__))
    logs_dir = os.path.join(work_dir, 'logs')
    if not os.path.isdir(logs_dir):
        os.makedirs(logs_dir)
    log_path = os.path.join(logs_dir, log_file_name)
    level = logging.INFO
    max_bytes = 200 * 1024 ** 2
    fh = RotatingFileHandler(
        log_path, maxBytes=max_bytes, backupCount=5)
    fh.setLevel(level)
    formatter = logging.Formatter('%(asctime)s %(name)s [%(levelname)s]:%(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
