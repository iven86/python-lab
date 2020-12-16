
import requests

r = requests.get('https://google.com')
print(r.headers)
print("==============================")
print(r.request.headers)