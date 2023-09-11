import requests

re = requests.get(url="https://webhook.site/0fb9254c-2d60-4dba-a305-980c1fabaf57")

print(re.status_code)
