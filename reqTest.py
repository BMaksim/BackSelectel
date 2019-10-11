import requests
r = requests.get('https://www.google.ru/')
print (r.text)