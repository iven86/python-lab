
import requests

r = requests.get(
    'https://google.com',
    cert=('/path/client.cert', '/path/client.key')
    )
print(r.headers)
print("==============================")
print(r.request.headers)