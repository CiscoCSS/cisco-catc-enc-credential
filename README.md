# dnac_encryption
Use Cryptography to encrypt credentials

Cisco DNA Center APIs Scripts can utilize encrypted credentials using cryptography's Fernet library in Python.

**Business Challenge:** Provide encrypted secured credentials while calling DNAC Api's
Goal: Use encrypted credentials in DNAC Api used scripts as well as provide a encryption method that meets vault, database or file store of the same. 
Example.

**Pre-requisite:** Python 3.8. If python is not installed, please follow: https://www.python.org/downloads/  
▪ pip3 or pip installed. If pip3 is not installed, please follow instructions at: https://pip.pypa.io/en/stable/installing/virtualenv installed 
▪ If virtualenv not installed already, install through bash$ pip3 install virtualenv. Follow this for further instructions: https://pypi.org/project/virtualenv/ 
▪ git installed ◦if git is not installed, please try referring: https://git-scm.com/downloads  
▪ Operating System: Linux based OS or windows

**Setup:**
▪python3 -m venv env3 
▪source env3/bin/activate
Run the command below with pip or pip3
▪pip install --upgrade pip 
▪pip install -r requirements.txt
or 
▪pip install --upgrade pip
▪pip install cryptography
▪pip install fernet

**Run your Script:**
Step 1. Generate key: python generate_key.py
Step 2. Generate encrypted user and password or credentials (Sanitize Prime): - python generate_enc_credentials.py
Step 3. Decrypt Credentials or Desanitize Prime: python decrypt_credentials.py 
Step 4. Use it with DNAC files. Add encrypted username enc_user1.txt password enc_pass1.txt copy to dnac_config file.
Step 5. On DNAC File that you run example dnac_file.py. Run DNAC file: python dnac_file.py
  519  python dnac_file_config.py
  520  python dnac_file_config.py
  521  vi 
  522  cat 
  523  python dnac_file_config.py
  524  pip freeze > requirements.txt
  525  cat requirements.txt 
  526  history

Step 2:
Cisco DNA Center License: This project is licensed to you under the terms of the Cisco Sample Code License.

Disclaimer: This document is Cisco Confidential information provided for your internal business use in connection with the Cisco Services purchased
by you or your authorized reseller on your behalf. This document contains guidance based on Cisco’s recommended practices. You remain responsible for 
determining whether to employ this guidance, whether it fits your network design, business needs, and whether the guidance complies with laws, 
including any regulatory, security, or privacy requirements applicable to your business.
