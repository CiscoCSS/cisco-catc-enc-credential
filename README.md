## cisco-catc-enc-credential

## Use Cryptography to Encrypt Catalyst Center Credentials

Cisco Catalyst Center Credentials can be encrypted using Fernet library in Python. Here is an example how to achieve same.


## Business Challenge
Provide encrypted secured credentials for accessing Catalyst Center via APIs.


## Goal
Use encrypted credentials for Catalyst Center APIs.

## Installation
Clone the repo
```bash
git clone https://github.com/CiscoCSS/cisco-catc-enc-credential.git
```
or Download as zip on your environment by clicking the option "code >> local >> Download as zip"

Go to your project folder
```bash
cd cisco-catc-enc-credential
```
Set up a Python venv First make sure that you have Python 3.8 installed on your machine. We will then be using venv to create an isolated environment with only the necessary packages.

## Pre-requisite
Python 3.8. If python is not installed, please follow:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

▪ pip3 or pip installed. If pip3 is not installed, please follow instructions at: 
[https://pip.pypa.io/en/stable/installing/virtualenv](https://pip.pypa.io/en/stable/installing/virtualenv)(https://pip.pypa.io/en/stable/installing/virtualenv) installed 

▪ If virtualenv not installed already, install through bash$ pip3 install virtualenv. Follow this for further instructions:
[https://pypi.org/project/virtualenv/](https://pypi.org/project/virtualenv/) 

▪ git installed
▪ if git is not installed, please try referring: 
[https://git-scm.com/downloads](https://git-scm.com/downloads)  

▪ Operating System: Linux based OS or windows

## Setup

Install virtualenv via pip
```bash
python3 -m venv env3 
```

Activate virtual environment
```bash
source env3/bin/activate
```

Run the command below with pip or pip3
```bash
pip install --upgrade pip 
```

```bash
pip install -r requirements.txt
```

or

```bash
pip install --upgrade pip
```

```bash
pip install cryptography
```

```bash
pip install fernet
```


## Run Script

### Step 1. 
Generate key: 

```bash
python generate_key.py
```

### Step 2. 
Generate encrypted user and password or credentials (Sanitize Prime):

```bash
python generate_enc_credentials.py
```

### Step 3. 
Decrypt Credentials or Desanitize Prime:

```bash
python decrypt_credentials.py
```

### Step 4. 
Use it with DNAC files. Add encrypted username dnac_enc_user1.txt password dnac_enc_pass1.txt copy to dnac_config file.
Modify variables
```
DNAC_URL_REGION1 = 'https://<ip address>' with your catalyst Center IP address, 
DNAC_USER_REGION1 = b'<copy and paste encrypted binary value here from dnac_enc_user1.txt, please keep the single quote and b>'
DNAC_PASS_REGION1 = b'<copy and paste encrypted binary value here from dnac_enc_pass1.txt, please keep the single quote and b>'
``` 

### Step 5. 
On DNAC File that you run example dnac_file.py. 
Run python file:

```bash
python dnac_file.py
```

### Step 6.

```bash
python dnac_encrypted.py
```        

Cisco DNA Center License: This project is licensed to you under the terms of the Cisco Sample Code License.

## Disclaimer

This document contains guidance based on Cisco’s recommended practices. You remain responsible for determining whether to employ this guidance,
whether it fits your network design, business needs, and whether the guidance complies with laws, including any regulatory, security, or privacy requirements applicable to your business.
