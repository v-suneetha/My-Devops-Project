import requests

# In this file we included redirection of output with in this file without using > redirection in linux to avoid encoding issues.
try:
    # Adding docker internal host url instead of localhost to make it work inside docker working directory.
    requests.post('http://host.docker.internal:8080/tasks', data="stay healthy")
    response = requests.get('http://host.docker.internal:8080/tasks', timeout=5)

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
