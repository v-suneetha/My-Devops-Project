import requests

try:
    # UnComment below code when you want to run it in docker workspace.
    '''requests.post('http://host.docker.internal:8080/tasks', data="stay healthy")
    response = requests.get('http://host.docker.internal:8080/tasks', timeout=5)'''
    
    # Updating url with kubernetes java-api-service to make it run inside kubernetes cluster.
    requests.post('http://java-api-service/tasks', data="stay healthy")
    response = requests.get('http://java-api-service/tasks', timeout=5)
    
    # In this file we included redirection of output with in this file without using > redirection in linux to avoid encoding issues.
    with open("python_alert_output.txt", "w", encoding="utf-8") as f:
        if response.status_code == 200:
            f.write("API is working\n")
            decoded_output = response.content.decode('utf-8', errors='replace')
            f.write("output: " + decoded_output + "\n")
        else:
            f.write("API is down\n")
except requests.exceptions.ConnectionError:
    with open("python_alert_output.txt", "w", encoding="utf-8") as f:
        f.write("API is down and Unreachable\n")
