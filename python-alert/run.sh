#!/bin/bash
pip install requests
python alert2.py 
python mail_alert.py
tail -f /dev/null


