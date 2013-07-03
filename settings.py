#!/usr/bin/python

from logging import getLogger, FileHandler, Formatter, INFO
from os.path import dirname,realpath
from os import makedirs
from base64 import b64decode
from sys import exit

# Logs
path = dirname(realpath(__file__))+'/'
path_log = path + 'logs/'
path_log_main = path_log + 'main.log'

logger = getLogger('my_log')
try:
    handler = FileHandler(path_log_main)
except Exception, e:
    makedirs(dirname(path_log_main))
    handler = FileHandler(path_log_main)
formatter = Formatter( '%(asctime)s - %(lineno)s: %(levelname)s %(message)s' )
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(INFO)

# Variables
ftp_user = ''
ftp_password = ''
ftp_host = ''
keep_for_months = 1
backup_name = 'backup'
directories = (
'/path/to/valuable/data',
)
