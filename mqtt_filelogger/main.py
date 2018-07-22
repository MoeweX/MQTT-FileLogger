# coding=utf-8
import logging

from mqtt_filelogger import CONFIG
from mqtt_filelogger.CSVStorageManager import CSVStorageManager
from mqtt_filelogger.MQTTProcessor import MQTTProcessor

LOG = logging.getLogger(__name__)

if __name__ == '__main__':
    # create objects
    csv_storage_manager = CSVStorageManager(CONFIG.base_directory_path)
    # csv_storage_manager.save_message("rsb/out", "message 1")
    # csv_storage_manager.save_message("rsb/out", "message 2")

    mqtt_processor = MQTTProcessor(csv_storage_manager)
    LOG.info("Started")

    # wait for user input to shut down application
    input()
    LOG.info("Shutting down")
