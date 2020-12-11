import requests
from requests.sessions import get_environ_proxies

proxy_list = {
    # http://free-proxy.cz/en/
    "https": "134.209.214.204:8080",
    "http": "13.92.119.142:80"
    # "https": "127.0.0.1:8080",
    # "http": "127.0.0.1:8080"
}

url = "https://google.com"
r = requests.get(url, proxies=proxy_list)
print(r.json)
# print(r.text)