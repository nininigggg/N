import requests


class TestAPI:
    def test_proxies(self):
        proxy = {
            "http": "http://127.0.0.1:8080",
            "https": "http://127.0.0.1:8080"
        }

        requests.post(url="", proxies=proxy, verify=False)


