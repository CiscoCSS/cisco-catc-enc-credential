
"""

Copyright (c) 2021 Cisco and/or its affiliates.

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
__copyright__ = "Copyright (c) {{current_year}} Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

from cryptography.fernet import Fernet
from dnac_config import DNAC_URL_REGION1, DNAC_PASS_REGION1, DNAC_USER_REGION1

FILE_DIR ='/<DIR PATH ABSOLUTE for Key File, username, password encrypted files/'
FILENAME = FILE_DIR + 'key.txt'
ENC_USER1_FILE = FILE_DIR + 'dnac_enc_user1.txt'
ENC_PASS1_FILE = FILE_DIR + 'dnac_enc_pass1.txt'

if __name__ == '__main__':
    #Add this to dnac_code
    #Read from a database or file
    with open(FILENAME, 'rb') as file_object:
        for line in file_object:
            enc_key = line
    #print(enc_key)
    #Get the read encrypted key and get the password entered when script is run
    cipher_suite = Fernet(enc_key)
    with open(ENC_USER1_FILE, 'rb') as file_object:
        for line in file_object:
            DNAC_USER_REGION1 = line
    uncipher_user1 = (cipher_suite.decrypt(DNAC_USER_REGION1))
    with open(ENC_PASS1_FILE, 'rb') as file_object:
        for line in file_object:
            DNAC_PASS_REGION1 = line
    uncipher_pwd1 = (cipher_suite.decrypt(DNAC_PASS_REGION1))
    plain_text_encusername = bytes(uncipher_user1).decode("utf-8")  # convert to string
    plain_text_encpassword = bytes(uncipher_pwd1).decode("utf-8")
    print(plain_text_encusername)
    print(plain_text_encpassword)

