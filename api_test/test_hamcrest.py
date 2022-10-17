import requests
from jsonpath import jsonpath
from hamcrest import *


class TestAPI:
    def test_hamcrest(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        print(r.text)
        assert_that(r.json()['category_list']['categories'][-3]['name'], equal_to('霍格沃兹测试开发学社'))

    def test_hogwarts_json(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        # assert r.json()['category_list']['categories'][0]['name'] == '霍格沃兹测试学院公众号'
        print(jsonpath(r.json(), '$..name'))
        assert jsonpath(r.json(), '$..name')[-3] == '霍格沃兹测试开发学社'