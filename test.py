import requests

print(requests.__version__)

people = requests.get("https://google.com")
print(people)
