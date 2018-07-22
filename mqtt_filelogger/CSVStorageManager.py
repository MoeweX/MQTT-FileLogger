import datetime
import logging
import os
import threading

LOG = logging.getLogger(__name__)


class CSVStorageManager:

    def __init__(self, basedir_path):
        self.__basedir_path = basedir_path
        self.__lock = threading.Lock()

        if not os.path.exists(basedir_path):
            os.makedirs(basedir_path)
            LOG.debug("Base directory did not exist, created it")

        LOG.debug("Started CSVStorageManager, basedir = {0}".format(basedir_path))

    def save_message(self, topic, message):
        self.__lock.acquire()
        LOG.info("Saving message with topic {0}".format(topic))
        try:
            file = self.__get_file(topic)
            now = datetime.datetime.now()
            time = now.strftime("%H:%M:%S")
            file.write("{0};{1}\n".format(time, message))
            file.close()
        finally:
            self.__lock.release()

    def __get_file(self, topic):
        # find directory of topic
        topic_dir_path = "{0}/{1}/".format(self.__basedir_path, topic)
        if not os.path.exists(topic_dir_path):
            os.makedirs(topic_dir_path)
            LOG.debug("Topic directory did not exist, created it")

        # find file in directory with current date
        now = datetime.datetime.now()
        file_path = "{0}{1}.csv".format(topic_dir_path, now.strftime("%Y%m%d"))

        if os.path.exists(file_path):
            mode = "a" # append if already exists
        else:
            mode = "w" # make a new file if not

        file = open(file_path,mode)

        # write header if not existed
        if mode == "w":
            file.write("time;message\n")

        # return file
        return file

