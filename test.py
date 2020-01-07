import requests

print(requests.__version__)

content = requests.get("https://raw.githubusercontent.com/aoladosu/Lab1/master/test.py?token=ALDMQMYLOY3BUT42FRHFWN26DXQLK")
print(content.content)
