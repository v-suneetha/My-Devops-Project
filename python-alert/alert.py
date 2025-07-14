import requests
import sys
import io

#With alert.py we need to redirect output using python alert.py > python_alert_output.txt file
#In this file we are getting issues with encoding UTF-8 even though fix is added and garbage characters are printing in output file.
# Force UTF-8 encoding for stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

try:
    requests.post('http://localhost:8080/tasks', data="stay healthy")
    response = requests.get('http://localhost:8080/tasks', timeout=5)
    if response.status_code == 200:
        print("API is working")
        decoded_output = response.content.decode('utf-8', errors='replace')
        print("output:", decoded_output)
    else:
        print("API is down")
except requests.exceptions.ConnectionError:
    print("API is down and Unreachable")

