# coding=utf-8
import toml


class Config(object):

    def __init__(self, config_file_name):
        dictionary = toml.load(config_file_name)

        mqtt = Config.get_value_or_default(dictionary, "mqtt")
        self.broker_address = Config.get_value_or_default(mqtt, "broker_address")
        csv = Config.get_value_or_default(dictionary, "csv")
        self.base_directory_path = Config.get_value_or_default(csv, "base_directory_path")

    @staticmethod
    def get_value_or_default(dictionary, field):
        try:
            return dictionary[field]
        except KeyError:
            return None
