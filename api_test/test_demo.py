import requests


def test_post_form():
    payload = {
        "level": 1,
        "name": "seveniruby"
    }
    r = requests.post("https://httpbin.org/post", data=payload)
    print(r.text)
    assert r.status_code == 200


def test_header():
    r = requests.get('https://httpbin.testing-studio.com/get', headers={"h": "header demo"})
    print(r.status_code)
    print(r.text)
    print(r.json())
    assert r.status_code == 200
    assert r.json()['headers']['H'] == "header demo"


def test_post_json():
    payload = {
        "level": 1,
        "name": "seveniruby"
    }
    r = requests.post("https://httpbin.org/post", json=payload)
    print(r.text)
    assert r.status_code == 200
    assert r.json()['json']['level'] == 1

