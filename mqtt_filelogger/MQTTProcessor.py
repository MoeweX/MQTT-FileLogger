# coding=utf-8
import logging

import paho.mqtt.client as mqtt

from mqtt_filelogger import CONFIG, CSVStorageManager

LOG = logging.getLogger(__name__)


class MQTTProcessor(object):

    def __init__(self, csv_storage_manager):
        self.__csv_storage_manager = csv_storage_manager

        self.__client = mqtt.Client("RemoteSwitchBricklet", clean_session=False)
        self.__client.connect(CONFIG.broker_address)

        self.__client.on_message = self.__on_message
        self.__client.subscribe("#")
        self.__client.loop_start()

        LOG.info("MQTTProcessor running")

    # noinspection PyUnusedLocal
    def __on_message(self, client, userdata, message):
        topic = message.topic
        payload = str(message.payload.decode("utf-8"))
        LOG.debug("Message topic: {0}".format(topic))
        LOG.debug("Message payload: {0}".format(payload))

        self.__csv_storage_manager.save_message(topic, payload)
