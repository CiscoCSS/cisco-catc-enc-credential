"""

Copyright (c) 2018 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Shirin Khan <shirkhan@cisco.com>"
__copyright__ = "Copyright (c) 2025 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

import argparse
import datetime
import logging
from cryptography.fernet import Fernet
from time import perf_counter as times

import urllib3
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import InsecureRequestWarning

import dnac_api as dnac_api
from dnac_config import DNAC_PASS_REGION1, DNAC_USER_REGION1, DNAC_URL_REGION1

urllib3.disable_warnings(InsecureRequestWarning)

FILE_DIR = '/Users/shirkhan/PycharmProjects/encryption/crypto/'
FILENAME = FILE_DIR + 'key.txt'
ENC_USER1_FILE = FILE_DIR + '/dnac_enc_user1.txt'
ENC_PASS1_FILE = FILE_DIR + '/dnac_enc_pass1.txt'


def get_device_list(dnac_auth, dnac_region1):
    """
    This function reads all devices in DNAC inventory and returns only wireless controller device list back
    :return: wireless controller device list on DNAC
    """

    # print(enc_key)
    # Get the read encrypted key and get the password entered when script is run
    bearer_token1 = dnac_api.get_dnac_jwt_token(dnac_auth, dnac_region1)
    total = dnac_api.get_network_device_count(bearer_token1, dnac_region1)
    logging.info('Total number of Devices: {total}')
    device_list = dnac_api.get_network_device_list(bearer_token1, dnac_region1, total)
    logging.info('Device_list: {device_list}')
    return device_list


if __name__ == '__main__':
    startTime = datetime.datetime.utcnow().strftime('%m-%d-%Y_%H%M%S.%f')[:-3]
    logging.basicConfig(
        # If you want to keep track in log then open this commented out application_run.log file
        #filename=LOG_FILENAME + '_'+ str(startTime) + '.log',
        # Logging INFO, ERROR, DEBUG
        level=logging.INFO,
        format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    # set logging to DEBUG based on CMD line args
    with open(FILENAME, 'rb') as file_object:
        for line in file_object:
            enc_key = line
    cipher_suite = Fernet(enc_key)
    user1 = (cipher_suite.decrypt(DNAC_USER_REGION1))
    pwd1 = (cipher_suite.decrypt(DNAC_PASS_REGION1))
    plain_text_enc_username = bytes(user1).decode("utf-8")  # convert to string
    plain_text_enc_password = bytes(pwd1).decode("utf-8")
    dnac_auth1 = HTTPBasicAuth(plain_text_enc_username, plain_text_enc_password)
    logging.info('Starting application .....')
    start = times()
    dev_list = get_device_list(dnac_auth1, DNAC_URL_REGION1)
    logging.info(f'Device List: {dev_list}')
