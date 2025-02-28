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

import getpass
from cryptography.fernet import Fernet

DNAC_USER1 = input('DNAC Username: ')
DNAC_PASS1 = getpass.getpass()
#if you want to keep key file in a different directory and user and password in a different directory then FILE_USERDIR to FILE_DIR and add the path
FILE_DIR = '/<Full path to Directory where Key file and user and password file path>/'
FILENAME = FILE_DIR + 'key.txt'
ENC_USER1_DNAC = FILE_DIR + 'dnac_enc_user1.txt'
ENC_PASS1_DNAC = FILE_DIR + 'dnac_enc_pass1.txt'

if __name__ == '__main__':
    credentials = {}
    #Add this to dnac_code
    #Read from a database or file
    with open(FILENAME, 'rb') as file_object:
        for line in file_object:
            enc_key = line
    #Get the read encrypted key and get the password entered when script is run
    cipher_suite = Fernet(enc_key)
    credentials['dnac_user1'] = cipher_suite.encrypt(bytes(DNAC_USER1, 'utf-8'))
    credentials['dnac_password1'] = cipher_suite.encrypt(bytes(DNAC_PASS1, 'utf-8'))
    with open(ENC_USER1_DNAC, 'wb') as writer:
        writer.write(credentials['dnac_user1'])
    with open(ENC_PASS1_DNAC, 'wb') as writer:
        writer.write(credentials['dnac_password1'])


