import requests
url = requests.get("https://xkcd.com/")
print(url.text)