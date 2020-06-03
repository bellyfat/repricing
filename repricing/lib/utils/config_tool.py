import os
from configparser import RawConfigParser


class ConfigTool(object):
    section = ""
    config = None
    default_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "config.ini")

    def __init__(self, file_path=None):
        if file_path is None:
            file_path = self.default_file_path
        self.config = RawConfigParser()
        self.config.read(file_path)
        self.file_path = file_path

    def set_section(self, section):
        self.section = section

    def get(self, key):
        if self.section:
            return self.config.get(self.section, key)
        else:
            return None

