import requests
try:
    response = requests.get('http://localhost:8080/tasks', timeout=5)
    if response.status_code == 200:
        print("API is working")
       
        print("output:", response.content)
    else:
        print("API is down")
except requests.exceptions.ConnectionError:
    print("API is down and Unreachable")

